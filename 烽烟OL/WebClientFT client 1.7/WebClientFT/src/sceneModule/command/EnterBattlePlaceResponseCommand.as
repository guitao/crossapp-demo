package sceneModule.command
{
	import com.hurlant.math.bi_internal;
	import proto.battle.battle703.InitBattleData;
	
	import event.GuidClearEvent;
	import event.GuidEventCenter;
	
	import flash.geom.Point;
	import flash.utils.ByteArray;
	
	import managers.WindowManager;
	
	import model.SystemDataModel;
	
	import mx.collections.ArrayCollection;
	
	import org.robotlegs.mvcs.Command;
	
	import proto.battle.battle703.BuffInfo;
	import proto.battle.battle703.EnemyArray;
	import proto.battle.battle703.FightData;
	import proto.battle.battle703.FightResponse;
	import proto.battle.battle703.Item;
	import proto.battle.battle703.SettlementData;
	
	import resource.CrotaItemConfig;
	
	import sceneModule.event.EnterBattlePlaceResponseEvent;
	import sceneModule.model.rvo.RBattleAllRoundVo;
	import sceneModule.model.rvo.RBattleBuffVo;
	import sceneModule.model.rvo.RBattleEnemyVo;
	import sceneModule.model.rvo.RBattleInitChaVo;
	import sceneModule.model.rvo.RBattleInitVo;
	import sceneModule.model.rvo.RBattleRoundVo;
	import sceneModule.model.vo.battleVo.BattleOverSettlementVo;
	import sceneModule.model.vo.itemsVo.AttributeVo;
	import sceneModule.model.vo.packageVo.PackageSuite;
	
	/**
	 * 获取玩家临时包裹栏中的物品 Command 
	 * @author Yaolx
	 * 
	 */	
	public class EnterBattlePlaceResponseCommand extends Command
	{
		[Inject]
		public var evt:EnterBattlePlaceResponseEvent;
		
		public function EnterBattlePlaceResponseCommand()
		{
		}
		//战场信息处理
		override public function execute():void{
			var responseData:proto.battle.battle703.FightResponse = evt.result;
			if(responseData.result && responseData.data){
				//初始化战场
				var initBattleVo:RBattleInitVo = new RBattleInitVo();
				if(responseData.data.startData){
					var bl:int = responseData.data.startData.length;
					var battleInitChaArr:Array = new Array();
					for(var bi:int=0;bi<bl;bi++){
						var initData:InitBattleData = responseData.data.startData[bi]
						var initBattleChaVo:RBattleInitChaVo = new RBattleInitChaVo();
						
						initBattleChaVo.chaId=initData.chaId;//角色的ID
						initBattleChaVo.chaBattleId=initData.chaBattleId;//角色的战场ID
						initBattleChaVo.chaName=initData.chaName;//角色的名称
						initBattleChaVo.chaLevel=initData.chaLevel;//角色的等级
						initBattleChaVo.chaProfessionType=initData.chaProfessionType;//角色的职业
						initBattleChaVo.chaDirection=initData.chaDirection;//1--玩家朝向右，朝向右。2--玩家朝向左
						initBattleChaVo.chaCurrentHp=initData.chaCurrentHp;//角色当前的血量
						initBattleChaVo.chaCurrentPower=initData.chaCurrentPower;//角色的当前能量
						initBattleChaVo.chaTotalHp=initData.chaTotalHp;//角色的总HP
						initBattleChaVo.chaTotalPower=initData.chaTotalPower;//角色的总Power
						if(SystemDataModel.roleId == initData.chaId){
							initBattleChaVo.chaIsMySelf=true;
						}else{
							initBattleChaVo.chaIsMySelf=false;
						}
						
						initBattleChaVo.chaPos =new Point(initData.chaPos[0],initData.chaPos[1]);//角色动画的坐标
						battleInitChaArr.push(initBattleChaVo);
					}
					initBattleVo.rBattleInitChaVoArr = battleInitChaArr;
					initBattleVo.rBattleCenterPoint = new Point(responseData.data.centerX,responseData.data.centerY);
					initBattleVo.rResArr = responseData.data.rResArr;
				}
				//战斗结算
				var bs:int = responseData.data.setData.length;
				SystemDataModel.battleInfoVo.battleResult = responseData.data.battleResult;
				SystemDataModel.battleInfoVo.fightType = responseData.data.fightType;
				var setDataArr:ArrayCollection = new ArrayCollection();
				for(var si:int=0;si<bs;si++){
					var settlementData:SettlementData = responseData.data.setData[si];
					var battleOverSettlementVo:BattleOverSettlementVo = new BattleOverSettlementVo();
						
						battleOverSettlementVo.id = settlementData.id;
						battleOverSettlementVo.coinBonus = settlementData.coinBonus;
					    battleOverSettlementVo.expBonus =settlementData.expBonus;
					    battleOverSettlementVo.goldBonus =settlementData.goldBonus;
						battleOverSettlementVo.attackGoal =settlementData.attackGoal;
						battleOverSettlementVo.defenseGoal=settlementData.defenseGoal;
//						battleOverSettlementVo.itemsBonus=settlementData.itemsBonus;
						battleOverSettlementVo.slayGoal=settlementData.slayGoal;
						battleOverSettlementVo.popularity = settlementData.popularity;
						battleOverSettlementVo.name = settlementData.name;
						battleOverSettlementVo.profession = settlementData.profession;
						if(settlementData.itemsBonus){
							var itemInfo:Item = settlementData.itemsBonus;
							battleOverSettlementVo.itemsBonus = CrotaItemConfig.getItemInfoByTempleteId(itemInfo.itemId);
							if(battleOverSettlementVo.itemsBonus){
								battleOverSettlementVo.itemsBonus.stack = itemInfo.stack;
							}
							
						}
						setDataArr.addItem(battleOverSettlementVo);
				}
				SystemDataModel.battleInfoVo.battleSettlementArr.source = setDataArr.toArray();
				//
				var battleAllRoundVo:RBattleAllRoundVo = new RBattleAllRoundVo();
				if(responseData.data.stepData){
					var sl:int = responseData.data.stepData.length;
					var battleRoundArray:Array = new Array();
					for( var ii:int=0;ii<sl;ii++){
						var fightData:FightData = responseData.data.stepData[ii];
							var rBattleRoundVo:RBattleRoundVo = new RBattleRoundVo();
							rBattleRoundVo.chaId = fightData.chaId;//角色的id
							rBattleRoundVo.chaBattleId = fightData.chaBattleId;//角色的战场ID
							rBattleRoundVo.chaProfessionType = fightData.chaProfessionType;//角色的职业
							rBattleRoundVo.actionId = fightData.actionId;//角色的攻击动作id
							rBattleRoundVo.counterHitActionId = fightData.counterHitActionId;//角色受反击时的动作
							
							rBattleRoundVo.isDeathOfCounterHit = fightData.isDeathOfCounterHit;//角色是否受反击致死0:否，1：是
							rBattleRoundVo.txtEffectId = fightData.txtEffectId;//角色的文字特效
							rBattleRoundVo.chaEffectId = fightData.chaEffectId;//角色特效ID
							rBattleRoundVo.chaEnemyEffectId = fightData.chaEnemyEffectId;//角色技能承受特效
							rBattleRoundVo.chaThrowEffectId = fightData.chaThrowEffectId;//角色技能投射特效
							rBattleRoundVo.chaAoeEffectId = fightData.chaAoeEffectId;//技能的全屏特效
							rBattleRoundVo.chaName = fightData.chaName;//名称
							rBattleRoundVo.chaLevel = fightData.chaLevel;//等级
							
							//buff
							var rl:int = fightData.chaBuffArr.length;
							var r_arr:Array = new Array();
							for(var ri:int=0;ri<rl;ri++){
								r_arr.push(fightData.chaBuffArr[ri]);
							}
							rBattleRoundVo.chaBuffArr = r_arr;
							//buffinfo
							var b_l:int = fightData.chaBuffShowList.length;
							var buff_arr:Array = new Array();
							for(var b_i:int=0;b_i<b_l;b_i++){
								var buffInfo:BuffInfo = fightData.chaBuffShowList[b_i];
								var rBattleBuffVo:RBattleBuffVo = new RBattleBuffVo();
								rBattleBuffVo.buffId = buffInfo.buffId;
								rBattleBuffVo.buffEffectId = buffInfo.buffId;
								rBattleBuffVo.buffIconId = buffInfo.buffId;
								rBattleBuffVo.buffName = buffInfo.buffName;
								rBattleBuffVo.buffLayerCount = buffInfo.buffLayerCount;
								rBattleBuffVo.buffRemainRoundCount = buffInfo.buffRemainRoundCount;
								buff_arr.push(rBattleBuffVo);
							}
							rBattleRoundVo.chaBuffShowList = buff_arr;
							
							
							
							rBattleRoundVo.chaPowerUp = fightData.chaPowerUp;//power增加
							rBattleRoundVo.chaPowerDown = fightData.chaPowerDown;//power减少(能量消耗)
							rBattleRoundVo.chaCurrentPower = fightData.chaCurrentPower;//当前的能量
							rBattleRoundVo.chaTotalPower = fightData.chaTotalPower;
							rBattleRoundVo.chaChangeHp = fightData.chaChangeHp;//角色血量变化(受治疗或攻击后)
							rBattleRoundVo.chaCurrentHp = fightData.chaCurrentHp;//角色当前的血量
							rBattleRoundVo.chaExpendHp = fightData.chaExpendHp;//角色血量消耗(技能消耗反弹等)
							
							rBattleRoundVo.chaStartPos = new Point(fightData.chaStartPos[0],fightData.chaStartPos[1]);//角色的起始坐标
							rBattleRoundVo.chaTargetPos = new Point(fightData.chaTargetPos[0],fightData.chaTargetPos[1]);//角色的目标坐标
							rBattleRoundVo.chaAttackType = fightData.chaAttackType;//角色的攻击方式 1:进程，2：远程
							rBattleRoundVo.chaDirection = fightData.chaDirection;//1玩家朝向右 2--玩家朝向左
							rBattleRoundVo.isCriticalBlow = fightData.isCriticalBlow;//是否暴击
							rBattleRoundVo.chaTotalHp = fightData.chaTotalHp;
//							repeated EnemyArray enemyChaArr = 25;//被攻击方数据
							var el:int = fightData.enemyChaArr.length;
							var eArr:Array = new Array();
							for(var ei:int=0;ei<el;ei++){
								var enemyInfo:EnemyArray = fightData.enemyChaArr[ei];
								var rBattleEnemyVo:RBattleEnemyVo = new RBattleEnemyVo();
								rBattleEnemyVo.enemyChaId = enemyInfo.enemyChaId;// ID
								rBattleEnemyVo.enemyBattleId = enemyInfo.enemyBattleId;// 战斗ID
//								trace("enemyBattleId"+enemyInfo.enemyBattleId);
								rBattleEnemyVo.enemyActionId = enemyInfo.enemyActionId;// 动作ID
								rBattleEnemyVo.enemyCounterHitActionId = enemyInfo.enemyCounterHitActionId;//反击时的动作ID
								rBattleEnemyVo.enemyTxtEffectId = enemyInfo.enemyTxtEffectId;// 文字效果ID，暴击，闪避，冰冻等
								
								rBattleEnemyVo.chaEffectId = enemyInfo.chaEffectId;//角色特效ID
								rBattleEnemyVo.chaEnemyEffectId = enemyInfo.chaEnemyEffectId;//被打角色特效ID
								rBattleEnemyVo.chaThrowEffectId = enemyInfo.chaThrowEffectId;//角色投射特效ID
								rBattleEnemyVo.chaEnemyAoeEffectId = enemyInfo.chaEnemyAoeEffectId;//受攻击者反击技能的全屏特效
								rBattleEnemyVo.enemyTotalHp = enemyInfo.enemyTotalHp;
								rBattleEnemyVo.enemyName = enemyInfo.enemyChaName;
								rBattleEnemyVo.enemyLevel = enemyInfo.enemychaLevel;
								//buff
								var rl1:int = enemyInfo.enemyBuffArr.length;
								var r_arr1:Array = new Array();
								for(var ri1:int=0;ri1<rl1;ri1++){
									r_arr1.push(enemyInfo.enemyBuffArr[ri1]);
								}
								rBattleEnemyVo.enemyBuffArr = r_arr1;
								//buffinfo
								var b_l1:int = enemyInfo.enemyBuffShowList.length;
								var buff_arr1:Array = new Array();
								for(var b_i1:int=0;b_i1<b_l1;b_i1++){
									var buffInfo1:BuffInfo = enemyInfo.enemyBuffShowList[b_i1];
									var rBattleBuffVo1:RBattleBuffVo = new RBattleBuffVo();
									rBattleBuffVo1.buffId = buffInfo1.buffId;
									rBattleBuffVo1.buffEffectId = buffInfo1.buffEffectId;
									rBattleBuffVo1.buffIconId = buffInfo1.buffIconId;
									rBattleBuffVo1.buffName = buffInfo1.buffName;
									rBattleBuffVo1.buffLayerCount = buffInfo1.buffLayerCount;
									rBattleBuffVo1.buffRemainRoundCount = buffInfo1.buffRemainRoundCount;
									buff_arr1.push(rBattleBuffVo1);
								}
								rBattleEnemyVo.enemyBuffShowList = buff_arr1;
								
								rBattleEnemyVo.enemyPowerUp = enemyInfo.enemyPowerUp;// +20 power增加
								rBattleEnemyVo.enemyCurrentPower = enemyInfo.enemyCurrentPower;//当前能量
								rBattleEnemyVo.enemyTotalPower = enemyInfo.enemyTotalPower;
								rBattleEnemyVo.enemyChangeHp = enemyInfo.enemyChangeHp;//角色血量变化
								rBattleEnemyVo.enemyCurrentHp = enemyInfo.enemyCurrentHp;//角色的当前血量
								rBattleEnemyVo.enemyCounterHit = enemyInfo.enemyCounterHit;// 是否反击：0-否，1-是
								rBattleEnemyVo.enemyStartPos = new Point(enemyInfo.enemyStartPos[0],enemyInfo.enemyStartPos[1]);// 起始坐标 
								rBattleEnemyVo.enemyTargetPos = new Point(enemyInfo.enemyTargetPos[0],enemyInfo.enemyTargetPos[1]);// 目标坐标
								rBattleEnemyVo.enemyDirection = enemyInfo.enemyDirection;//1--玩家朝向右，朝向右。2--玩家朝向左
								rBattleEnemyVo.enemyProfessionType = enemyInfo.enemyProfessionType;//1--玩家朝向右，朝向右。2--玩家朝向左
								eArr.push(rBattleEnemyVo);
							}
							rBattleRoundVo.enemyChaArr = eArr;
							battleRoundArray.push(rBattleRoundVo);
							battleAllRoundVo.rBattleAllRoundArr = battleRoundArray;
//							battleAllRoundVo.rSceneId = responseData.data.
					}
				}
				WindowManager.closeAllWindows();
				GuidEventCenter.getInstance().dispatchEvent(new GuidClearEvent(GuidClearEvent.INTO_FIGHT));
				SystemDataModel.isBattleStatusFlag = true;
			}
		}
	}
}