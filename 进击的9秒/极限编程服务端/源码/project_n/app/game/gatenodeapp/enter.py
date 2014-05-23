#coding:utf8
'''
Created on 2013-10-25

@author: lan (www.9miao.com)
'''
from app.game.gatenodeservice import remoteserviceHandle
from app.game.core.character.PlayerCharacter import PlayerCharacter
from app.game.core.PlayersManager import PlayersManager



@remoteserviceHandle
def enterPlace_601(dynamicId, characterId, placeId,force,player):
    '''进入场景'''
    if not player:
        player = PlayerCharacter(characterId,dynamicId = dynamicId)
    PlayersManager().addPlayer(player)
    playerinfo = player.formatInfo()
    responsedata = {'result':True,'message':'',
                    'data':{'cid':playerinfo['id'],
                            'name':playerinfo['nickname'],
                            'score':playerinfo['score']}
                    }
    return responsedata

                    
