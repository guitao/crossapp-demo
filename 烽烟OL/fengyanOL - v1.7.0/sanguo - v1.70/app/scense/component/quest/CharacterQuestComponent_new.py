#coding:utf8
'''
Created on 2011-11-29

@author: lan
'''
from app.scense.component.Component import Component
from app.scense.component.quest.Quest import Quest
from app.scense.utils.dbopera import dbtask,dbNpc
from app.scense.protoFile.quest import TaskTracNotify1421_pb2,TaskFinshNotify1422_pb2
from twisted.python import log
from app.scense.serverconfig.node import pushObjectByCharacterId
from app.scense.netInterface.pushObjectNetInterface import pushCorpsApplication
from app.scense.core.language.Language import Lg

MAXREWARDQUESTCOUNT = 10#任务进行中的最大数量
TRACKMAXCOUNT = 5#任务追踪的最大数量
TASK_ERROR = 0 #任务错误状态
TASK_ACCEPTABLE = 1 #任务可接状态
TASK_PROCESSING = 2 #任务进行状态
TASK_CANCOMMITED = 3 #任务可提交状态
TASK_EXEC = 4 #任务执行状态（需要对话）
NPC_NONE = 0 #npc无任务时的状态标识
NPC_ACCEPTABLE = 1 #npc有可接任务时的状态标识
NPC_PROCESS = 2 #npc有进行中任务时的状态标识
NPC_CANCOMMITED = 3 #npc有可提交任务时的状态标识
NPC_EXEC = 2 #npc有需要对话的任务时的状态标识
#任务状态对应的NPC状态
STATUSMAP = {TASK_ERROR:NPC_NONE, 
             TASK_ACCEPTABLE:NPC_ACCEPTABLE,
             TASK_PROCESSING:NPC_PROCESS,
             TASK_CANCOMMITED:NPC_CANCOMMITED,
             TASK_EXEC:NPC_EXEC}

def pushScenceNpcQuestStatus(stausList,dynamicId):
    '''推送场景中NPC的任务状态'''
    from app.scense.protoFile.quest import getScenceNpcQuestStatus_pb2
    response = getScenceNpcQuestStatus_pb2.getScenceNpcQuestStatusResponse()
    for statu in stausList:
        npcStatu = response.NPCQuestStatusList.add()
        npcStatu.npcID = statu['npcID']
        npcStatu.statu = statu['statu']
    msg = response.SerializeToString()
    pushObjectByCharacterId(1408,msg,[dynamicId])
        
def pushTaskCanFinished(sendList):
    '''推送任务已完成的消息
    '''
    response = TaskFinshNotify1422_pb2.TaskFinshNotify()
    msg = response.SerializeToString()
    pushObjectByCharacterId(1422, msg, sendList)

def pushQuestProcessList(data,dynamicId):
    '''推送任务追踪信息
    @param data: 追踪的信息
    @param dynamicId: 客户端的动态ID
    '''
    response  = TaskTracNotify1421_pb2.TaskTracListNotify()
    cur_list = data.get('cur_list')
    acceptable_list = data.get('acceptable_list')
    for task in cur_list:
        taskResponse = response.cur_list.add()
        taskResponse.is_trac = task.get('is_trac')
        taskResponse.task_id = task.get('task_id')
        taskResponse.task_state = task.get('task_state')
        taskResponse.task_accpet_npc_id = task.get('task_accpet_npc_id')
        taskResponse.cur_num = task.get('cur_num')
        taskResponse.need_num = task.get('need_num')
        taskResponse.task_running_des = task.get('task_running_des')
        taskResponse.task_complete_des = task.get('task_complete_des')
        taskResponse.task_name = task.get('task_name')
        for runningargs in task.get('runing_args'):
            runing_arg = taskResponse.runing_args.add()
            runing_arg.id = runningargs.get('id')
            runing_arg.label = runningargs.get('label')
        for completeargs in task.get('complete_args'):
            complete_arg = taskResponse.complete_args.add()
            complete_arg.id = completeargs.get('id')
            complete_arg.label = completeargs.get('label','')
            
    for task in acceptable_list:
        taskResponse = response.acceptable_list.add()
        taskResponse.task_id = int(task.format.get('taskID'))
        taskResponse.task_name = task.format.get('taskName')
        taskResponse.task_accpet_npc_id = task.format.get('providerNPC')
        taskResponse.task_accpet_city_id = task.format.get('providerScene')
        taskResponse.need_lv = int(task.format.get('levelRequired'))
    msg = response.SerializeToString()
    pushObjectByCharacterId(1421, msg, [dynamicId])
    

class CharacterQuestComponent(Component):
    """templateInfo component for character"""

    def __init__(self, owner):
        '''
        Constructor
        '''
        Component.__init__(self, owner)
        self._npcList = [] #当前场景的npc列表
        self._tasks = {} #角色正在进行的任务
        self._finished = []#角色已完成的任务列表
#        self._canaccept = []#可接受的任务的列表

    def initCharacterQuest(self):
        '''初始化角色任务'''
        characterId = self._owner.baseInfo.id
        processlist = dbtask.getAllProcessInfo(characterId)
        for process in processlist:
            questId = process.get('taskId')
            if process['finished']:
                self._finished.append(questId)
                continue
            quest = Quest(questId,characterId = self._owner.baseInfo.id)
            quest.initQuestData(process)
            quest.setProfession(self._owner.profession.getProfession())
            self._tasks[questId] = quest
            
    def setNpcList(self,npcList):
        '''设置当前场景中的NPC列表'''
        self._npcList = npcList
        
    def getQuestOnNpc(self,npcId):
        '''获取Npc身上的列表
        @param npcId: int npc的id
        '''
        allMainTask = dbtask.ALL_MAIN_TASK
        allExtenTask = dbtask.ALL_EXTEN_TASK
        taskInfolist = allMainTask.values() + allExtenTask.values()
        cancomlist = []#可以提交的
        canacceptlist = []#可以接受的
        doinglist = []#进行中的
        execlist = []#需要对话的任务
        for taskinfo in taskInfolist:
            taskId = taskinfo['taskID']
            if taskinfo['providerNPC']==npcId:#npc作为提供任务的npc时
                if self.canReceived(taskId):
                    canacceptlist.append(taskId)
                    break
            if taskinfo['demandNPC']==npcId and taskId in self._tasks.keys():#npc作为对话任务的npc时
                if not self.canCommited(taskId):
                    execlist.append(taskId)
                    break
            #npc作为结束任务的npc时
            if taskinfo['reporterNPC']==npcId and taskId in self._tasks.keys():
                if self.canCommited(taskId):
                    cancomlist.append(taskId)
                else:
                    doinglist.append(taskId)
        info = {}
        goallenght = len(cancomlist)+len(doinglist)+ len(canacceptlist)
        if goallenght>3:
            dd = 3 - goallenght
        else:
            dd = 3
        info['cancomlist'] = cancomlist
        info['canacceptlist'] = canacceptlist[:dd]
        info['doinglist'] = doinglist
        info['execlist'] = execlist
        return info
    
    def getCanReceivedQuestList(self):
        '''获取可接任务列表'''
        canReceivedQuestList = []
        allMainTask = dbtask.ALL_MAIN_TASK
        allExtenTask = dbtask.ALL_EXTEN_TASK
        tasklist = allMainTask.keys()+allExtenTask.keys()
        for taskid in tasklist:
            if self.canReceived(taskid):
                self.autoApplyQuest(taskid)
#                taskInfo = Quest( taskid, characterId = self._owner.baseInfo.id,status=1)
#                taskInfo.setProfession(self._owner.profession.getProfession())
#                canReceivedQuestList.append(taskInfo)
        return canReceivedQuestList
    
    def autoApplyQuest(self,taskId):
        '''自动接受任务
        '''
        characterId = self._owner.baseInfo.id
        if not self.canReceived(taskId):
            return {'result':False,'message':Lg().g(444),\
                    'task_id':taskId}
        task = Quest(taskId,characterId = characterId)
        task.setProfession(self._owner.profession.getProfession())
        result = self.giveItemHandle(taskId)
        if not result.get('result'):
            return result
        res = task.InsertProcess()
        if res:
            self._tasks[taskId] = task

    def canReceived(self,taskID):
        '''判断任务是否可接(普通的任务，包括主线与支线)
        @param taskId: taskId int 任务的id 
        '''
        allMainTask = dbtask.ALL_MAIN_TASK
        allExtenTask = dbtask.ALL_EXTEN_TASK
        if taskID < 20000:
            taskInfo = allMainTask.get(taskID)
        else:
            taskInfo = allExtenTask.get(taskID)
        level = self._owner.level.getLevel()
        profession = self._owner.profession.getProfession()
        if not taskInfo:
            return False
        #判断任务是否已经完成过
        if taskInfo['taskID'] in self._finished:
            return False
        #判断任务是否已经接受
        if taskInfo['taskID'] in self._tasks.keys():
            return False
        #判断等级是否符合
        if taskInfo['levelRequired']> level:
            return False
        #判断职业是否符合
        if taskInfo['professionRequired'] and taskInfo['professionRequired']!=profession:
            return False
        #判断前置任务
        if taskInfo['priorityID']!=0 and taskInfo['priorityID'] not in self._finished:
            return False
        return True
        
    def canCommited(self,taskId):
        '''查看任务是否可以提交
        @param taskId: int 任务的ID
        '''
        task = self._tasks.get(taskId)
        if not task:
            return False
        if task._finishedState:
            return eval(task._finishedState)
        taskInfo = task.format
        taskprocess = task.process
        if taskInfo.get('taskType',1)==1:
            if taskprocess['talkCount']>=1:
                return True
        elif taskInfo.get('taskType',1)==2:
            if taskprocess['killCount']>=taskInfo['monsterCount']:
                return True
            return False
        elif taskInfo.get('taskType',1)==3:
            if taskprocess['checkpointCount']>0:
                return True
            return False
        elif taskInfo.get('taskType',1)==4:
            if taskprocess['goldCount']>=taskInfo['demandGold']:
                return True
            return False
        elif taskInfo.get('taskType',1)==5:
            package = self._owner.pack._package.getPackageByType(2)
            if package.countItemTemplateId(taskInfo['demandItem'])>=taskInfo['itemCount']:
                return True
            return False
        elif taskInfo.get('taskType',1)==6:#通关战役任务
            if taskprocess['checkpointCount']>0 or self._owner.zhanyi.checkClean(taskInfo['demandCheckpoint']):
                return True
            return False
        else:
            if taskprocess['talkCount']>0:
                return True
            return False
        return False
        
    def applyQuest(self,taskId,taskType = 1):
        '''接受任务
        @param taskId: int 任务的id
        '''
        allMainTask = dbtask.ALL_MAIN_TASK
        allExtenTask = dbtask.ALL_EXTEN_TASK
        if taskId < 20000:
            taskInfo = allMainTask.get(taskId)
        else:
            taskInfo = allExtenTask.get(taskId)
        characterId = self._owner.baseInfo.id
        if not self.canReceived(taskId):
            return {'result':False,'message':Lg().g(444),\
                    'task_id':taskId}
        task = Quest(taskId,characterId = characterId)
        task.setProfession(self._owner.profession.getProfession())
        result = self.giveItemHandle(taskId)
        if not result.get('result'):
            return result
        res = task.InsertProcess()
        if res:
            if res and taskType==1:
                self._tasks[taskId] = task
            self.pushPlayerScenceNpcQuestStatus()
            self.pushPlayerQuestProcessList()
            return {'result':True,'message':Lg().g(445)%taskInfo['taskName'],\
                    'task_id':taskId}
        return {'result':False,'message':Lg().g(444),\
                'task_id':taskId}
        
    def commitQuest(self,taskId,npcId,taskType = 1):
        '''提交任务
        @param taskId: int 任务的id
        @param chooseId: int 选择任务物品的id
        '''
        if not self.canCommited(taskId): #判断是否满足完成条件
            return {'result':False,'message':Lg().g(446)}
        characterId = self._owner.baseInfo.id
        #-------*--获取任务的奖励---*-----#
        result = self.questBoundHandle(taskId)#任务奖励处理
        if not result.get('result'):
            return result
        dbtask.UpdateTaskProcess(characterId, taskId,{'finished':1})
        del self._tasks[taskId]
        self._finished.append(taskId)
        self.pushPlayerScenceNpcQuestStatus()
        self.pushPlayerQuestProcessList()
        if taskId<20000:
            taskInfo = dbtask.ALL_MAIN_TASK.get(taskId)
        else:
            taskInfo = dbtask.ALL_EXTEN_TASK.get(taskId)
        itemTemplateID = taskInfo.get('demandItem',0)
        self.clearQuestItem(itemTemplateID)
        if taskId>=20000:
            self._owner.daily.noticeDaily(16,0,-1)
        return {'result':True,'message':Lg().g(447)}
    
    def abandonQuest(self,taskId):
        '''放弃任务
        @param taskId: int 任务的id
        '''
        ret = dbtask.DelTaskProcessInfo(self._owner.baseInfo.id, taskId)
        if not ret:
            return {'result':False,'message':Lg().g(448)}
        return {'result':False,'message':Lg().g(448)}
        del self._tasks[taskId]
        self.pushPlayerScenceNpcQuestStatus()
        self.pushPlayerQuestProcessList()
        if taskId<20000:
            taskInfo = dbtask.ALL_MAIN_TASK.get(taskId)
        else:
            taskInfo = dbtask.ALL_EXTEN_TASK.get(taskId)
        itemTemplateID = taskInfo.get('demandItem',0)
        itemTemplateID1 = taskInfo.get('giveItem',0)
        self.clearQuestItem(itemTemplateID )
        self.clearQuestItem(itemTemplateID1)
        return {'result':True,'message':Lg().g(449)}
    
    def updateQuestTraceStatu(self,taskID,trackStatu):
        '''更新任务追踪状态'''
        task = self._tasks.get(taskID)
        if not task:
            return {'result':False}
        result = task.updateTrack(trackStatu)
        if result:
            self.pushPlayerQuestProcessList()
            return {'result':True}
        return {'result':False}
        
    def getExpBouns(self,Exp):
        '''获取经验奖励'''
        self._owner.level.updateExp(self._owner.level.getExp()+Exp)
        
    def getCoinBouns(self,Coin):
        '''获取金币奖励'''
        self._owner.finance.addCoin(Coin)
        
    def getGoldBouns(self,Gold):
        '''获取钻奖励'''
        self._owner.finance.addGold(Gold)
        
    def getOneNpcState(self,npcID):
        '''获取当个NPC的头顶任务状态
        @param npcID: int npc的ID
        '''
        tasks = self.getQuestOnNpc(npcID)
        if tasks['cancomlist']:
            return NPC_CANCOMMITED
        elif tasks['canacceptlist']:
            return NPC_ACCEPTABLE
        elif tasks['doinglist']:
            return NPC_PROCESS
        elif tasks['execlist']:
            return NPC_PROCESS
        else:
            return NPC_NONE
    
    def getPlayerScenceNpcQuestStatus(self):
        '''获取场景中NPC的任务状态标识
        @param npcList: 
        '''
        statusList = []
        for npcID in self._npcList:
            statusInfo = {}
            statusInfo['npcID'] = npcID
            statusInfo['statu'] = self.getOneNpcState(npcID)
            statusList.append(statusInfo)
        return statusList
    
    def getTaskProcessInfo(self):
        '''获取所有的进行的任务列表'''
        return self._tasks.values()
    
    def pushPlayerScenceNpcQuestStatus(self):
        '''推送场景中npc的任务状态'''
        statusList = self.getPlayerScenceNpcQuestStatus()
        pushScenceNpcQuestStatus(statusList,self._owner.baseInfo.id)
        
    def getQuestProcessList(self):
        '''获取任务进度列表'''
        processList = []
        for task in self._tasks.values():
            processtask = task.process
            processInfo = {}
            taskInfo = task.format
            processInfo['is_trac']= task.getTrack()
            processInfo['task_id'] = taskInfo['taskID']
            hasFinished = 2
            if self.canCommited(taskInfo['taskID']):
                hasFinished = 3
            processInfo['task_state'] = hasFinished
            processInfo['task_name'] = taskInfo['taskName']
            processInfo['task_accpet_npc_id'] = taskInfo['providerNPC']
#            if taskInfo['taskType']==1:#任务是谈话任务时
#                processInfo['need_num'] = 1
#                processInfo['cur_num'] = 1#processtask['talkCount']
            if taskInfo['taskType']==2:#任务时杀怪任务时
                processInfo['need_num'] = taskInfo['monsterCount']
                processInfo['cur_num'] = processtask['killCount']
            elif taskInfo['taskType']==3:#任务时通关任务时
                processInfo['need_num'] = 1
                processInfo['cur_num'] = processtask['checkpointCount']
            elif taskInfo['taskType']==4:#任务是使用消耗钻任务时
                processInfo['need_num'] = taskInfo['demandGold']
                processInfo['cur_num'] = processtask['goldCount']
            elif taskInfo['taskType']==5:#任务是收集任务时
                processInfo['need_num'] = taskInfo['itemCount']
                package = self._owner.pack._package.getPackageByType(2)
                processInfo['cur_num'] = package.countItemTemplateId(taskInfo['demandItem'])
            elif taskInfo['taskType']==6:#任务是收集任务时
                processInfo['need_num'] = 1
                processInfo['cur_num'] = 1 if hasFinished==3 else processtask['talkCount']
            else:
                processInfo['need_num'] = 1
                processInfo['cur_num'] = processtask['talkCount']
            processInfo['task_running_des'] = taskInfo['task_running_des']
            processInfo['task_complete_des'] = taskInfo['task_complete_des']
            processInfo['runing_args'] = []
            processInfo['complete_args'] = []
            for i in range(1,6):
                running_arg = {}
                complete_args = {}
                running_arg['id'] = taskInfo.get('running_int_arg%d'%i,0)
                running_arg['label'] = taskInfo.get('running_char_arg%d'%i,'')
                complete_args['id'] = taskInfo.get('complete_int_arg%d'%i,'')
                complete_args['label'] = taskInfo.get('complete_char_arg%d'%i,'')
                processInfo['runing_args'].append(running_arg)
                processInfo['complete_args'].append(complete_args)
            processList.append(processInfo)
        return processList
    
    def pushPlayerQuestProcessList(self):
        '''推送自身任务进度列表信息'''
        data = {}
        self.getCanReceivedQuestList()
        cur_list = self.getQuestProcessList()
        acceptable_list = []
        data['cur_list'] = cur_list
        data['acceptable_list'] = acceptable_list
        pushQuestProcessList(data,self._owner.baseInfo.id)
        
    ######################任务过程处理##############################

    def talkWithNpc(self,npcId,taskId):
        '''与Npc交谈(传话任务的处理)
        @param npcId: int npc的id 
        '''
        task = self._tasks.get(taskId)
        if not task:
            return False
        taskInfo = task.format
        if taskInfo['demandNPC']!=npcId:
            return False
        task = self._tasks[taskId]
        props = {'talkCount':1}
        task.updateProcess(props)
        self.commitQuest(task._id, 0)#如果任务完成自动提交任务
        self.pushPlayerScenceNpcQuestStatus()
        self.pushPlayerQuestProcessList()
        return True
        
    def killMonster(self,monsterId):
        '''杀怪处理
        @param monsterId: int 怪物的id
        '''
        tag = 0
        finishend = 0
        for task in self._tasks.values():
            process = task.process
            taskInfo = task.format
            if taskInfo['demandMonster']!=monsterId and taskInfo['itemRelationMonster']!=monsterId:
                continue
            if taskInfo['taskType']==2:
                needprocesscnt = taskInfo.get('monsterCount')
                nowprocesscnt = process.get('killCount')
                if nowprocesscnt < needprocesscnt:
                    tag = 1
                    newprocesscnt = nowprocesscnt + 1
                    props = {'killCount':newprocesscnt}
                    task.updateProcess(props)
                    if newprocesscnt == needprocesscnt:
                        finishend = 1
            if taskInfo['taskType']==5:
                package = self._owner.pack._package.getPackageByType(2)
                nowCount =  package.countItemTemplateId(taskInfo['demandItem'])
                needprocesscnt = taskInfo.get('itemCount')
                if nowCount < needprocesscnt:
                    tag = 1
                    newprocesscnt = nowCount+1
                    props = {'collectCount':newprocesscnt}
                    self._owner.pack.putNewItemsInPackage(taskInfo['demandItem'],1)
                    task.updateProcess(props)
                    if newprocesscnt == needprocesscnt:
                        finishend = 1
                    self.commitQuest(task._id, 0)#如果任务完成自动提交任务
        if tag:
            self.pushPlayerScenceNpcQuestStatus()
            self.pushPlayerQuestProcessList()
            if finishend:
                self._owner.msgbox.putSpecialMsg(2)
            
    def clearance(self,instanceID):
        '''通关副本的处理
        @param instanceID: int 副本的ID
        '''
        tag = 0
        for task in self._tasks.values():
            taskInfo = task.format
            process = task.process
            if taskInfo['taskType']!= 3:
                continue
            if taskInfo['demandCheckpoint']!=instanceID:
                continue
            if process.get('checkpointCount')<1:
                tag = 1
                props = {'checkpointCount':1}
                task.updateProcess(props)
                self.commitQuest(task._id, 0)#如果任务完成自动提交任务
        if tag:
            self.pushPlayerScenceNpcQuestStatus()
            self.pushPlayerQuestProcessList()
            self._owner.msgbox.putSpecialMsg(2)
            
    def cleanZhanYi(self,zhangjieid):
        '''通关战役的处理
        '''
        tag = 0
        for task in self._tasks.values():
            taskInfo = task.format
            process = task.process
            if taskInfo['taskType']!= 6:
                continue
            if taskInfo['demandCheckpoint']!=zhangjieid:
                continue
            if process.get('checkpointCount')<1:
                tag = 1
                props = {'checkpointCount':1}
                task.updateProcess(props)
                self.commitQuest(task._id, 0)#如果任务完成自动提交任务
        if tag:
            self.pushPlayerScenceNpcQuestStatus()
            self.pushPlayerQuestProcessList()
            self._owner.msgbox.putSpecialMsg(2)
            
    def UseGold(self,goldCount):
        '''消耗钻的处理
        @param goldCount: int 钻的数量
        '''
        tag = 0
        finishend = 0
        for task in self._tasks.values():
            taskInfo = task.format
            process = task.process
            if taskInfo['taskType']!= 4:
                continue
            needprocesscnt = taskInfo.get('demandGold')
            nowprocesscnt = process.get('goldCount')
            if nowprocesscnt < needprocesscnt:
                tag = 1
                newprocesscnt = nowprocesscnt + goldCount
                props = {'goldCount':newprocesscnt}
                task.updateProcess(props)
                if newprocesscnt >=needprocesscnt:
                    finishend = 1
                    self.commitQuest(task._id, 0)#如果任务完成自动提交任务
        if tag:
            self.pushPlayerScenceNpcQuestStatus()
            self.pushPlayerQuestProcessList()
            if finishend:
                self._owner.msgbox.putSpecialMsg(2)
                
    ##########################################################
    
    def giveItemHandle(self,taskId,taskType = 1):
        '''接受任务时给予物品的处理'''
        taskInfo = Quest( taskId)
        taskInfo.setProfession(self._owner.profession.getProfession())
        giveitems = taskInfo.resolveGiveItem()
        package = self._owner.pack._package.getPackageByType(1)
        bagCnt = package.findSparePositionNum()#包裹的格子剩余数量
        if len(giveitems)>bagCnt:
            return {'result':False,'message':Lg().g(16)}
        for item in giveitems:
            self._owner.pack.putNewItemInPackage(item)
        return {'result':True}
        
    def questBoundHandle(self,taskId,taskType = 1):
        '''任务奖励处理
        @param taskId: int 任务的奖励
        '''
        taskInfo = Quest( taskId)
        taskInfo.setProfession(self._owner.profession.getProfession())
        giveitems = taskInfo.resolveItemPrize()
        package = self._owner.pack._package.getPackageByType(1)
        bagCnt = package.findSparePositionNum()#包裹的格子剩余数量
        if len(giveitems)>bagCnt:
            return {'result':False,'message':Lg().g(16)}
        for item in giveitems:
            self._owner.pack.putNewItemInPackage(item)
            self.AfterGetNewEqupment(item)
        exp = taskInfo.format.get('ExpPrize')
        self.getExpBouns(exp)
        coin = taskInfo.format.get('CoinPrize')
        self.getCoinBouns(coin)
        gold = taskInfo.format.get('GoldPrize')
        self.getGoldBouns(gold)
        return {'result':True}

            
    def specialTaskHandle(self,TaskType,state = 1):
        '''特殊任务处理'''
        tag = 0
        for task in self._tasks.values():
            taskInfo = task.format
            if taskInfo.get('taskType')!=TaskType:
                continue
            process = task.process
            if process['talkCount']>0:
                continue
            if task._finishedState:
                if self.canCommited(task._id):
                    props = {'talkCount':1}
                    task.updateProcess(props)
                    tag = 1
                    self.commitQuest(task._id, 0)#如果任务完成自动提交任务
            else:
                props = {'talkCount':1}
                task.updateProcess(props)
                tag = 1
                self.commitQuest(task._id, 0)#如果任务完成自动提交任务
        if tag:
            self.pushPlayerQuestProcessList()
            self.pushPlayerScenceNpcQuestStatus()
            if state:
                self.pushTaskCanFinished()
            else:
                self._owner.msgbox.putSpecialMsg(2)
            
    def clearQuestItem(self,itemTemplateID,count=1):
        '''清除任务物品
        @param itemTemplateID: int 物品的id
        '''
        package = self._owner.pack._package.getPackageByType(2)
#        nowCount =  package.countItemTemplateId(itemTemplateID)
        positions = package.getItemTemplateIdPositions(itemTemplateID)
        for item in positions:
            package.deleteItemInPackage(item['position'])
        
    def formatNpcQuestInfo(self,NpcId):
        '''格式化NPC任务信息
        @param tasks: list(int) 任务列表
        @param NpcId: int NPC的ID
        @param status: int  0非法 1可接  2进行中 3完成
        '''
        npcInfo = dbNpc.ALL_NPCS.get(NpcId)
        if not npcInfo:
            log.err(u'坑爹呢NpcID不正确:%d'%NpcId)
            return {}
        NpcQuestInfo = {}
        NpcQuestInfo['npc_id'] = NpcId
        NpcQuestInfo['npc_img'] = npcInfo.get('resourceid',0)
        NpcQuestInfo['npc_name'] = npcInfo.get('name',u'配置有误')
        NpcQuestInfo['npc_word'] = npcInfo.get('dialog',u'配置有误,id为%d的NPC不存在'%NpcId)
        NpcQuestInfo['ncp_task_item'] = []
        tasks = self.getQuestOnNpc(NpcId)
        for taskId in tasks['cancomlist']:
            taskInfo = Quest( taskId,status = TASK_CANCOMMITED)
            taskInfo.setNpcName(npcInfo.get('name',u'配置有误'))
            taskInfo.setRoleName(self._owner.baseInfo.getName())
            taskInfo.setProfession(self._owner.profession.getProfession())
            NpcQuestInfo['ncp_task_item'].append(taskInfo)
        for taskId in tasks['execlist']:
            taskInfo = Quest( taskId,status = TASK_EXEC)
            taskInfo.setNpcName(npcInfo.get('name',u'配置有误'))
            taskInfo.setRoleName(self._owner.baseInfo.getName())
            taskInfo.setProfession(self._owner.profession.getProfession())
            NpcQuestInfo['ncp_task_item'].append(taskInfo)
        for taskId in tasks['canacceptlist']:
            taskInfo = Quest( taskId,status = TASK_ACCEPTABLE)
            taskInfo.setNpcName(npcInfo.get('name',u'配置有误'))
            taskInfo.setRoleName(self._owner.baseInfo.getName())
            taskInfo.setProfession(self._owner.profession.getProfession())
            NpcQuestInfo['ncp_task_item'].append(taskInfo)
        for taskId in tasks['doinglist']:
            taskInfo = Quest( taskId,status = TASK_PROCESSING)
            taskInfo.setNpcName(npcInfo.get('name',u'配置有误'))
            taskInfo.setRoleName(self._owner.baseInfo.getName())
            taskInfo.setProfession(self._owner.profession.getProfession())
            NpcQuestInfo['ncp_task_item'].append(taskInfo)
        return NpcQuestInfo
        
    def pushTaskCanFinished(self):
        '''推送任务已完成的消息
        '''
        response = TaskFinshNotify1422_pb2.TaskFinshNotify()
        response.finshID = 0
        msg = response.SerializeToString()
        pushObjectByCharacterId(1422, msg, [self._owner.baseInfo.id])

    def AfterGetNewEqupment(self,item):
        '''获取新的装备奖励后的处理'''
        toposition = item.baseInfo.getItemBodyType()
        if toposition==-1:
            return
        recCharacterId = self._owner.baseInfo.id
        sysOpeType = 1
        tishiStr = Lg().g(450)
        contentStr = Lg().g(451)
        caozuoStr = Lg().g(452)
        icon = item.baseInfo.getItemTemplateInfo().get('icon',0)
        itype = item.baseInfo.getItemTemplateInfo().get('type',0)
        package = self._owner.pack._package.getPropsPagePack()
        realpos = package.getPositionByItemId(item.baseInfo.id)
        curPage = realpos/30+1
        pos = realpos%30
        pushCorpsApplication(recCharacterId, sysOpeType, tishiStr,
                              contentStr, caozuoStr, icon = icon,
                              type = itype, pos = pos, curPage= curPage,
                              toposition = toposition)
    
    
