"""
Created by Velocity-plus
Github: https://github.com/Velocity-plus/css-flashbot

Date: 21-06-2015

Comments has been removed!
"""


import es
import esc
import playerlib
import gamethread
import popuplib
from vecmath import vector
import vecmath


bot_data = {}

def load():
    global bot_data
    esc.msg('#255,255,0[Bot Flasher] #0,0,0Has been loaded')



def player_activate(ev):
    userid = ev["userid"]
    steamid = es.getplayersteamid(userid)
    bot.reset_properties(steamid)


class BotApi:
    def __init__(self):
        global bot_data

    def reset_properties(self, steamid):
        if steamid not in bot_data:

            bot_data[steamid] = {}

            bot_data[steamid]['CLIENT_LOCATION'] = (0,0,0)
            bot_data[steamid]['CLIENT_VELOCITY'] = False
            bot_data[steamid]['CLIENT_BOOST_COUNT'] = 0
            bot_data[steamid]['CLIENT_TIMER'] = 0


            bot_data[steamid]['BOT_1'] = {}

            bot_data[steamid]['BOT_1']['BOT_STYLE'] = 0
            bot_data[steamid]['BOT_1']['BOT_MODE'] = 0
            bot_data[steamid]['BOT_1']['BOT_DIFFICULTY'] = 0
            bot_data[steamid]['BOT_1']['BOT_SHARE'] = 0
            bot_data[steamid]['BOT_1']['BOT_CROUCHED'] = False
            bot_data[steamid]['BOT_1']['BOT_LOCATION'] = (0,0,0)
            bot_data[steamid]['BOT_1']['BOOST_ANGLE'] = (0,0,0)
            bot_data[steamid]['BOT_1']['BOOST_COUNT'] = 0
            bot_data[steamid]['BOT_1']['ID'] = 1
            bot_data[steamid]['BOT_1']['BOOST_VALID'] = False

            bot_data[steamid]['BOT_2'] = {}

            bot_data[steamid]['BOT_2']['BOT_STYLE'] = 0
            bot_data[steamid]['BOT_2']['BOT_MODE'] = 0
            bot_data[steamid]['BOT_2']['BOT_DIFFICULTY'] = 0
            bot_data[steamid]['BOT_2']['BOT_SHARE'] = 0
            bot_data[steamid]['BOT_2']['BOT_CROUCHED'] = False
            bot_data[steamid]['BOT_2']['BOT_LOCATION'] = (0,0,0)
            bot_data[steamid]['BOT_2']['BOOST_ANGLE'] = (0,0,0)
            bot_data[steamid]['BOT_2']['BOOST_COUNT'] = 0
            bot_data[steamid]['BOT_2']['BOOST_VALID'] = False

    def boost(self, userid, bot_pointer):
        """
        :param steamid: Vailding boost
        :param func: Function call
        :param args: Arguements for function call
        :param bot: Which bot it points to
        :return: None
        """
        bot_id = ('BOT_%s' % bot_pointer)
        steamid = es.getplayersteamid(userid)

        org_pos = bot_data[steamid][bot_id]['BOT_LOCATION']
        change_pos = es.getplayerlocation(userid)  # Tuple
        cha_x_coordi = int(change_pos[0])
        cha_y_coordi = int(change_pos[1])
        cha_z_coordi = int(change_pos[2])

        if bot_data[steamid][bot_id]['BOT_CROUCHED']:
            if 120 > -org_pos[2] - (-cha_z_coordi) and 120 > -cha_z_coordi - (-org_pos[2]) and 85 > -cha_x_coordi - (
            -org_pos[0]) and 85 > -org_pos[0] - (-cha_x_coordi) and 85 > -org_pos[1] - (
            -cha_y_coordi) and 85 > -cha_y_coordi - (-org_pos[1]):
                if steamid not in bot_data:
                    print('BotApi().boost %s IS NOT VALIDED!!' % steamid)

                return [True, bot_id]

            else: return [False, bot_id]

        else:

            if 115 > -org_pos[2] - (-cha_z_coordi) and 115 > -cha_z_coordi - (-org_pos[2]) and 85 > -cha_x_coordi - (
            -org_pos[0]) and 85 > -org_pos[0] - (-cha_x_coordi) and 85 > -org_pos[1] - (
            -cha_y_coordi) and 85 > -cha_y_coordi - (-org_pos[1]):
                if steamid not in bot_data:
                   print('BotApi().boost %s IS NOT VALIDED!!' % steamid)


                get_prec = round((-org_pos[2] - (-cha_z_coordi)) * 0.87, 2)

                if get_prec >= 60:
                    return [True, bot_id]
                else:return [False, bot_id]


            else: return [False, bot_id]

    def boost_share(self, userid, target, bot_pointer):
        """
        :param steamid: Vailding boost
        :param func: Function call
        :param args: Arguements for function call
        :param bot: Which bot it points to
        :return: None
        """
        bot_id = ('BOT_%s' % bot_pointer)
        steamid = es.getplayersteamid(userid)

        org_pos = bot_data[steamid][bot_id]['BOT_LOCATION']
        change_pos = es.getplayerlocation(target)  # Tuple
        cha_x_coordi = int(change_pos[0])
        cha_y_coordi = int(change_pos[1])
        cha_z_coordi = int(change_pos[2])

        if bot_data[steamid][bot_id]['BOT_CROUCHED']:
            if 120 > -org_pos[2] - (-cha_z_coordi) and 120 > -cha_z_coordi - (-org_pos[2]) and 85 > -cha_x_coordi - (
            -org_pos[0]) and 85 > -org_pos[0] - (-cha_x_coordi) and 85 > -org_pos[1] - (
            -cha_y_coordi) and 85 > -cha_y_coordi - (-org_pos[1]):
                if steamid not in bot_data:
                    print('BotApi().boost %s IS NOT VALIDED!!' % steamid)

                return [True, bot_id]

            else: return [False, bot_id]

        else:

            if 115 > -org_pos[2] - (-cha_z_coordi) and 115 > -cha_z_coordi - (-org_pos[2]) and 85 > -cha_x_coordi - (
            -org_pos[0]) and 85 > -org_pos[0] - (-cha_x_coordi) and 85 > -org_pos[1] - (
            -cha_y_coordi) and 85 > -cha_y_coordi - (-org_pos[1]):
                if steamid not in bot_data:
                   print('BotApi().boost %s IS NOT VALIDED!!' % steamid)


                get_prec = round((-org_pos[2] - (-cha_z_coordi)) * 0.87, 2)

                if get_prec >= 60:
                    return [True, bot_id]
                else:return [False, bot_id]


            else: return [False, bot_id]


    def remove_bot_model(self, userid, bot_pointer=1):
            steamid = es.getplayersteamid(userid)
            bot_id = bot_pointer
            entList = es.createentitylist()
            for entIndex in dict(entList):
                    if es.entitygetvalue(entIndex, 'targetname') == ('BOT_ID_%s_%s' % (bot_id, userid)):

                        es.server.queuecmd('es_remove %s' % entIndex)
                    if es.entitygetvalue(entIndex, 'targetname') == ('BOT_ID_%s_%s' % (bot_id - 1, userid)):

                        es.server.queuecmd('es_remove %s' % entIndex)


    def reset_reasonable_data(self, userid):
        steamid = es.getplayersteamid(userid)

        # CLIENT
        bot_data[steamid]['CLIENT_VELOCITY'] = False
        bot_data[steamid]['CLIENT_BOOST_COUNT'] = 0
        bot_data[steamid]['CLIENT_TIMER'] = 0
        bot_data[steamid]['BOT_1']['BOOST_COUNT'] = 0
        bot_data[steamid]['BOT_2']['BOOST_COUNT'] = 0

        # BOT

    def create_bot_model(self, userid, set_location, crouched=False, bot_pointer=1):
            steamid = es.getplayersteamid(userid)
            bot_id = bot_pointer

            es.precachemodel('models/player/ct_sas.mdl')
            index = es.createentity('prop_dynamic')
            es.entitysetvalue(index, 'targetname', 'BOT_ID_%s_%s' % (str(bot_id), userid))
            es.entitysetvalue(index,'model','models/player/ct_sas.mdl')
            if crouched:
                bot_data[steamid]["BOT_1"]['BOT_CROUCHED'] = True
                es.entitysetvalue(index, 'origin',"%s %s %s" % (set_location[0], set_location[1], set_location[2] - 24))  # set its location to the player's
            else:
                bot_data[steamid]["BOT_1"]['BOT_CROUCHED'] = False
                es.entitysetvalue(index, 'origin',"%s %s %s" % (set_location[0], set_location[1], set_location[2] - 4))

            es.server.queuecmd('es_xspawnentity %s' % index)




    def create_bot_model_share(self, userid, set_location, crouched=False, bot_pointer=1):
            bot_id = bot_pointer
            steamid = es.getplayersteamid(userid)
            es.precachemodel('models/player/ct_sas.mdl')
            index = es.createentity('prop_dynamic')
            es.entitysetvalue(index, 'targetname', 'BOT_ID_%s_%s' % (bot_id, userid))
            es.entitysetvalue(index,'model','models/player/ct_sas.mdl')
            if crouched:
                bot_data[steamid]["BOT_%s" % bot_id]['BOT_CROUCHED'] = True
                es.entitysetvalue(index, 'origin',"%s %s %s" % (set_location[0], set_location[1], set_location[2] - 24))  # set its location to the player's
            else:
                bot_data[steamid]["BOT_%s" % bot_id]['BOT_CROUCHED'] = False
                es.entitysetvalue(index, 'origin',"%s %s %s" % (set_location[0], set_location[1], set_location[2] - 4))
            es.entitysetvalue(index,'rendercolor','255 0 0')
            es.server.queuecmd('es_xspawnentity %s' % index)





bot = BotApi()


def getPushAngle(userid, view_angle, horiz, vert, vert_override=False):
    """

    Pushes the player along his or her view vector.

    Call without underscore, i.e.: player.push(horiz, vert, vert_override)

    """

    myVector = view_angle

    horzX = float(horiz) * float(myVector[0])

    horzY = float(horiz) * float(myVector[1])

    if str(vert_override) == '0':

        vertZ = float(myVector[2]) * float(vert)

    else:

        vertZ = vert

    myNewVector = es.createvectorstring(horzX, horzY, vertZ)

    es.setplayerprop(userid, "CBasePlayer.localdata.m_vecBaseVelocity", myNewVector)



def boost_properties(userid, bot_pointer, velocity, velocity_xy, velocity_z):
    bot_id = bot_pointer
    steamid = es.getplayersteamid(userid)
    data = bot_data[steamid][bot_id]
    location = es.getplayerlocation(userid)
    FORMAT1 = (data['BOT_LOCATION'][0], data['BOT_LOCATION'][1], data['BOT_LOCATION'][2])
    FORMAT2 = (bot_data[steamid]["CLIENT_LOCATION"][0], bot_data[steamid]["CLIENT_LOCATION"][1], bot_data[steamid]["CLIENT_LOCATION"][2])
    DISTANCE = int(vecmath.distance(FORMAT1, FORMAT2))

    if DISTANCE > 1000:
        DISTANCE = 1000

    if DISTANCE < 60:
        esc.tell(userid, '#255,255,0** BOT ** You jumped too close to the bot.')
        return

    if DISTANCE > 60 and DISTANCE <= 80:
        DISTANCE = 0

    if bot_data[steamid]["CLIENT_BOOST_COUNT"] > 1 or not bot_data[steamid][bot_id]["BOT_CROUCHED"]:
        if DISTANCE > 300:
            getPushAngle(userid, data['BOOST_ANGLE'], (velocity_xy + velocity_z + 2228) * 0.30, (1050 + abs(velocity_z)) - 75, True)

        else:
            getPushAngle(userid, data['BOOST_ANGLE'], (velocity_xy + velocity_z + 2228 + DISTANCE) * 0.225 , (1085 + abs(velocity_z * 1.05)) - (DISTANCE * 3), True)

    else:
      if DISTANCE > 0:
        getPushAngle(userid, data['BOOST_ANGLE'], velocity + (DISTANCE * 2), (1000) - (DISTANCE * 3), True)
      else:
        getPushAngle(userid, data['BOOST_ANGLE'], velocity * 0.65, (1000 - (DISTANCE * 4)), True)





def player_say(ev):
    userid = ev["userid"]
    steamid = es.getplayersteamid(userid)
    player = playerlib.getPlayer(userid)
    bot_id = 0
    target = es.getplayerlocation(userid)
    text = ev["text"]
    if text == "!bot":
        menu_bot_main(userid)
    if text == "!log":
        bot.reset_properties(steamid)
        es.msg('logged!')


def menu_bot_main(userid):
    steamid = es.getplayersteamid(userid)
    data = bot_data[steamid]["BOT_1"]
    if steamid in bot_data:
        info = popuplib.create('menu_bot_main')
        info.addline('Boost Booster ')
        info.addline('- Properties')
        info.addline('________________________')
        info.addline('->1. <Place Bot 1>')
        info.addline('->2. Crouch: %s' % data['BOT_CROUCHED'])
        info.addline('->3. Share Bot: %s' % bot_data[steamid]["BOT_1"]['BOT_SHARE'])
        info.addline('________________________')
        info.addline('->4. <Place Bot 2>')
        info.addline('->5. Share Bot: %s' % bot_data[steamid]["BOT_1"]['BOT_SHARE'])
        info.addline(' ')
        if bot_data[steamid]['BOT_1']['BOT_MODE'] == 1:
            info.addline('->6. Mode (On)')
        else:
            info.addline('->6. Mode (Off)')
        info.addline(' ')
        info.addline('Made by Velo++')
        info.addline('0. Exit')
        info.enablekeys = "123456708"
        info.unsend(userid)
        info.send(userid)
        info.delete()
        info.menuselect = menu_bot_main_select
    else: esc.msg('You are not logged')


def menu_bot_main_select(userid, choice, popupid):
    steamid = es.getplayersteamid(userid)
    player = playerlib.getPlayer(userid)
    if int(choice) == 1:
        bot.remove_bot_model(userid, 1)
        bot_data[steamid]['BOT_1']['BOT_CROUCHED'] = True
        bot_data[steamid]['BOT_1']['BOOST_ANGLE'] = player.viewVector()
        bot_data[steamid]['BOT_1']['BOT_LOCATION'] = es.getplayerlocation(userid)
        if bot_data[steamid]['BOT_1']['BOT_SHARE'] == 1:
            if bot_data[steamid]['BOT_1']['BOT_CROUCHED']:
                bot.create_bot_model_share(userid,bot_data[steamid]['BOT_1']['BOT_LOCATION'],True, 1)

            else:
                bot.create_bot_model_share(userid,bot_data[steamid]['BOT_1']['BOT_LOCATION'],False, 1)

            esc.tell(userid, '#255,255,0** NOTICE ** (BOT 1) Boost Angle is set to where you are pointing!')
        else:
            if bot_data[steamid]['BOT_1']['BOT_CROUCHED']:
                bot.create_bot_model(userid,bot_data[steamid]['BOT_1']['BOT_LOCATION'],True, 1)

            else:
                bot.create_bot_model(userid,bot_data[steamid]['BOT_1']['BOT_LOCATION'],False, 1)
            esc.tell(userid, '#255,255,0** NOTICE ** (BOT 1) Boost Angle is set to where you are pointing!')
        menu_bot_main(userid)



    if int(choice) == 2:
        bot.remove_bot_model(userid, 1)
        if bot_data[steamid]['BOT_1']['BOT_SHARE'] == 1:
            if not bot_data[steamid]['BOT_1']['BOT_CROUCHED']:
                bot_data[steamid]['BOT_1']['BOT_CROUCHED'] = True
                bot.create_bot_model_share(userid,bot_data[steamid]['BOT_1']['BOT_LOCATION'],True, 1)
            else:
                bot_data[steamid]['BOT_1']['BOT_CROUCHED'] = False
                bot.create_bot_model_share(userid,bot_data[steamid]['BOT_1']['BOT_LOCATION'],False, 1)
        else:
            if not bot_data[steamid]['BOT_1']['BOT_CROUCHED']:
                bot_data[steamid]['BOT_1']['BOT_CROUCHED'] = True
                bot.create_bot_model(userid,bot_data[steamid]['BOT_1']['BOT_LOCATION'],True, 1)
            else:
                bot_data[steamid]['BOT_1']['BOT_CROUCHED'] = False
                bot.create_bot_model(userid,bot_data[steamid]['BOT_1']['BOT_LOCATION'],False, 1)

        menu_bot_main(userid)


    if int(choice) == 3:
        bot.remove_bot_model(userid, 1)
        if bot_data[steamid]['BOT_1']['BOT_SHARE'] == 0:
            bot_data[steamid]['BOT_1']['BOT_SHARE'] = 1
            if bot_data[steamid]['BOT_1']['BOT_CROUCHED']:
                bot.create_bot_model_share(userid,bot_data[steamid]['BOT_1']['BOT_LOCATION'],True, 1)

            else:
                bot.create_bot_model_share(userid,bot_data[steamid]['BOT_1']['BOT_LOCATION'],False, 1)
            gamethread.cancelDelayed("Ticker_Public_%s" % userid)
            Ticker_Public(userid, 1)

            esc.tell(userid, '#255,255,0** SHARE ** (BOT 1) Other people can now use your bot')
        else:
            bot_data[steamid]['BOT_1']['BOT_SHARE'] = 0
            gamethread.cancelDelayed("Ticker_Public_%s" % userid)
            if bot_data[steamid]['BOT_1']['BOT_CROUCHED']:
                bot.create_bot_model(userid,bot_data[steamid]['BOT_1']['BOT_LOCATION'],True, 1)

            else:
                bot.create_bot_model(userid,bot_data[steamid]['BOT_1']['BOT_LOCATION'],False, 1)
            esc.tell(userid, '#255,255,0** SHARE ** (BOT 1) You have toggled shared off')

        menu_bot_main(userid)

    if int(choice) == 4:
        bot.remove_bot_model(userid, 2)
        bot_data[steamid]['BOT_2']['BOT_CROUCHED'] = True
        bot_data[steamid]['BOT_2']['BOOST_ANGLE'] = player.viewVector()
        bot_data[steamid]['BOT_2']['BOT_LOCATION'] = es.getplayerlocation(userid)
        if bot_data[steamid]['BOT_2']['BOT_SHARE'] == 1:
            bot.create_bot_model_share(userid,bot_data[steamid]['BOT_2']['BOT_LOCATION'],False, 2)
            esc.tell(userid, '#255,255,0** NOTICE ** (BOT 2) Boost Angle is set to where you are pointing!')
        else:
            bot.create_bot_model(userid,bot_data[steamid]['BOT_2']['BOT_LOCATION'],False, 2)
            esc.tell(userid, '#255,255,0** NOTICE ** (BOT 2) Boost Angle is set to where you are pointing!')
        menu_bot_main(userid)

    if int(choice) == 5:
        bot.remove_bot_model(userid, 2)
        if bot_data[steamid]['BOT_2']['BOT_SHARE'] == 0:
            bot_data[steamid]['BOT_2']['BOT_SHARE'] = 1
            if bot_data[steamid]['BOT_2']['BOT_CROUCHED']:
                bot.create_bot_model_share(userid,bot_data[steamid]['BOT_2']['BOT_LOCATION'],True, 2)

            else:
                bot.create_bot_model_share(userid,bot_data[steamid]['BOT_2']['BOT_LOCATION'],False, 2)

            esc.tell(userid, '#255,255,0** SHARE ** (BOT 2) Other people can now use your bot')
        else:
            bot_data[steamid]['BOT_2']['BOT_SHARE'] = 0
            if bot_data[steamid]['BOT_2']['BOT_CROUCHED']:
                bot.create_bot_model(userid,bot_data[steamid]['BOT_2']['BOT_LOCATION'],True, 2)

            else:
                bot.create_bot_model(userid,bot_data[steamid]['BOT_2']['BOT_LOCATION'],False, 2)
            esc.tell(userid, '#255,255,0** SHARE ** (BOT 2) You have toggled shared off')

        menu_bot_main(userid)

    if int(choice) == 6:
      if bot_data[steamid]['BOT_1']['BOT_MODE'] == 0:
        bot_data[steamid]['BOT_1']['BOT_MODE'] = 1
        esc.tell(userid, '#255,255,0** BOT ** Toggled On')
      else:
         bot_data[steamid]['BOT_1']['BOT_MODE'] = 0
         esc.tell(userid, '#255,255,0** BOT ** Toggled Off')
      menu_bot_main(userid)






def Ticker_Client(userid, time):
    steamid = es.getplayersteamid(userid)
    player = playerlib.getPlayer(userid)
    velocity = int(round(vector((float(es.getplayerprop(userid, 'CBasePlayer.localdata.m_vecVelocity[0]')),
                                 float(es.getplayerprop(userid, 'CBasePlayer.localdata.m_vecVelocity[1]')),
                                 float(es.getplayerprop(userid,
                                                        'CBasePlayer.localdata.m_vecVelocity[2]')))).length(),
                         2))
    velocity_z = int(es.getplayerprop(userid, 'CBasePlayer.localdata.m_vecVelocity[2]'))
    velocity_xy = int(
        vector(float(es.getplayerprop(userid, 'CBasePlayer.localdata.m_vecVelocity[0]')), float(
            es.getplayerprop(userid, 'CBasePlayer.localdata.m_vecVelocity[1]'))).length())
    if player.onGround():
            bot.remove_bot_model(userid, 1)
            if bot_data[steamid]['BOT_1']['BOT_SHARE'] == 1:
                bot.create_bot_model_share(userid,bot_data[steamid]['BOT_1']['BOT_LOCATION'],True, 1)
            else:
                bot.create_bot_model(userid,bot_data[steamid]['BOT_1']['BOT_LOCATION'],True, 1)

            return

    if bot.boost(userid, 1)[0] and time <= 0:
        bot_data[steamid]["BOT_1"]["BOOST_COUNT"] += 1
        bot_data[steamid]['CLIENT_BOOST_COUNT'] += 1
        if bot_data[steamid]["CLIENT_BOOST_COUNT"] > 1:
              if velocity_xy >= 400:
                boost_properties(userid, bot.boost(userid, 1)[1],velocity, velocity_xy,velocity_z)
                esc.tell(userid, '#255,255,0NICE #255,0,0X%s #cyan#PRO Precision' % bot_data[steamid]["CLIENT_BOOST_COUNT"])
              else:
                esc.tell(userid, '#255,255,0You are cheating #cyan(TOTAL #255,0,0X%s #cyanWITHOUT CHEAT)' % (bot_data[steamid]["CLIENT_BOOST_COUNT"] - 1))
                bot.remove_bot_model(userid, 1)
                bot.create_bot_model(userid,bot_data[steamid]['BOT_1']['BOT_LOCATION'],True, 1)
                gamethread.cancelDelayed('Ticker_Client_%s' % userid)
                return

        else:
            esc.tell(userid, '#255,255,0NICE #255,0,0X%s #cyan#PRO Precision' % bot_data[steamid]["CLIENT_BOOST_COUNT"])
            boost_properties(userid, bot.boost(userid, 1)[1],velocity, velocity_xy,velocity_z)



        gamethread.cancelDelayed('Ticker_Client_%s' % userid)
        if bot_data[steamid]['CLIENT_BOOST_COUNT'] == 1:
            if bot_data[steamid]["BOT_1"]["BOT_SHARE"] == 1:
                bot.remove_bot_model(userid, 1)
                bot.create_bot_model_share(userid,bot_data[steamid]['BOT_1']['BOT_LOCATION'],False, 1)

            else:
                bot.remove_bot_model(userid, 1)
                bot.create_bot_model(userid,bot_data[steamid]['BOT_1']['BOT_LOCATION'],False, 1)


        Ticker_Client(userid, 1)
        return

    if bot.boost(userid, 2)[0] and time <= 0:
        bot_data[steamid]["BOT_2"]["BOOST_COUNT"] += 1
        bot_data[steamid]['CLIENT_BOOST_COUNT'] += 1
        if bot_data[steamid]["CLIENT_BOOST_COUNT"] > 1:
              if velocity_xy >= 400:
                boost_properties(userid, bot.boost(userid, 2)[1],velocity, velocity_xy,velocity_z)
                esc.tell(userid, '#255,255,0NICE #255,0,0X%s #cyan#PRO Precision' % bot_data[steamid]["CLIENT_BOOST_COUNT"])
              else:
                esc.tell(userid, '#255,255,0You are cheating #cyan(TOTAL #255,0,0X%s #cyanWITHOUT CHEAT)' % (bot_data[steamid]["CLIENT_BOOST_COUNT"] - 1))
                bot.remove_bot_model(userid, 1)
                bot.create_bot_model(userid,bot_data[steamid]['BOT_1']['BOT_LOCATION'],True, 1)
                gamethread.cancelDelayed('Ticker_Client_%s' % userid)
                return

        else:
            esc.tell(userid, '#255,255,0NICE #255,0,0X%s #cyan#PRO Precision' % bot_data[steamid]["CLIENT_BOOST_COUNT"])
            boost_properties(userid, bot.boost(userid, 2)[1],velocity, velocity_xy,velocity_z)



        gamethread.cancelDelayed('Ticker_Client_%s' % userid)
        if bot_data[steamid]['CLIENT_BOOST_COUNT'] == 1:
            if bot_data[steamid]["BOT_2"]["BOT_SHARE"] == 1:
                bot.remove_bot_model(userid, 2)
                bot.create_bot_model_share(userid,bot_data[steamid]['BOT_2']['BOT_LOCATION'],False, 2)

            else:
                bot.remove_bot_model(userid, 2)
                bot.create_bot_model(userid,bot_data[steamid]['BOT_2']['BOT_LOCATION'],False, 2)

        Ticker_Client(userid, 1)
        return



        #if bot.boost(userid, 2)[0] and time <= 0:
           # boost_properties(userid, bot.boost(userid, 2)[1])

    time -= 0.01


    gamethread.delayedname(0.001, 'Ticker_Client_%s' % userid, Ticker_Client, args=(userid, time))



def Ticker_Public(userid, time):
         steamid = es.getplayersteamid(userid)
         for userid_share in es.getUseridList():
             if not userid == userid_share:
                steamid_share = es.getplayersteamid(userid_share)
                if steamid_share in bot_data:
                    if bot_data[steamid_share]['BOT_1']['BOT_MODE'] == 1:
                        """
                        velocity_share = int(round(vector((float(es.getplayerprop(userid_share, 'CBasePlayer.localdata.m_vecVelocity[0]')),
                                                     float(es.getplayerprop(userid_share, 'CBasePlayer.localdata.m_vecVelocity[1]')),
                                                     float(es.getplayerprop(userid_share,
                                                                            'CBasePlayer.localdata.m_vecVelocity[2]')))).length(),
                                             2))
                        velocity_z_share = int(es.getplayerprop(userid_share, 'CBasePlayer.localdata.m_vecVelocity[2]'))
                        velocity_xy_share = int(
                            vector(float(es.getplayerprop(userid_share, 'CBasePlayer.localdata.m_vecVelocity[0]')), float(
                                es.getplayerprop(userid_share, 'CBasePlayer.localdata.m_vecVelocity[1]'))).length())
                        """
                        if bot.boost_share(userid, userid_share, 1)[0] and time <= 0:
                            bot_data[steamid_share]['CLIENT_BOOST_COUNT'] += 1
                            if bot_data[steamid_share]["CLIENT_BOOST_COUNT"] > 1:
                                esc.tell(userid_share, '#255,255,0NICE #255,0,0X%s #cyan#PRO Precision' % bot_data[steamid_share]["CLIENT_BOOST_COUNT"])
                                # boost_properties(userid_share, bot.boost(userid_share, 1)[1],velocity_share, velocity_xy_share,velocity_z_share)

                            else:
                                esc.tell(userid_share, '#255,255,0NICE #255,0,0X%s #cyan#PRO Precision' % bot_data[steamid_share]["CLIENT_BOOST_COUNT"])
                               # boost_properties(userid_share, bot.boost(userid_share, 1)[1],velocity_share, velocity_xy_share,velocity_z_share)

                            gamethread.cancelDelayed('Ticker_Public_%s' % userid)
                            Ticker_Public(userid, 1)
                            return


         gamethread.delayedname(0.001, 'Ticker_Public_%s' % userid, Ticker_Public, args=(userid, time))


def player_jump(ev):
    userid = ev['userid']
    steamid = es.getplayersteamid(userid)
    player = playerlib.getPlayer(userid)
    if steamid in bot_data:
        if bot_data[steamid]['BOT_1']['BOT_MODE'] == 1 or bot_data[steamid]['BOT_2']['BOT_MODE'] == 1:
            bot.reset_reasonable_data(userid)
            bot_data[steamid]['CLIENT_LOCATION'] = es.getplayerlocation(userid)
            data = bot_data[steamid]["BOT_1"]
            location = es.getplayerlocation(userid)
            FORMAT1 = (data['BOT_LOCATION'][0], data['BOT_LOCATION'][1], data['BOT_LOCATION'][2])
            FORMAT2 = (bot_data[steamid]["CLIENT_LOCATION"][0], bot_data[steamid]["CLIENT_LOCATION"][1], bot_data[steamid]["CLIENT_LOCATION"][2])
            DISTANCE = int(vecmath.distance(FORMAT1, FORMAT2))
            if DISTANCE > 240 + 32:
                bot.remove_bot_model(userid, 1)
                bot.create_bot_model(userid,bot_data[steamid]['BOT_1']['BOT_LOCATION'],False, 1)
            Ticker_Client(userid, 0.3)
            data = bot_data[steamid]["BOT_1"]

