# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "damre"
__date__ = "$19-dic-2016 11.45.30$"

import telepot
import time

bot = telepot.Bot('305631478:AAE0_VCwW3qUD6i4WNA2IcVVPwevLqlKLUs')
print(bot.getMe())
users = list()

def handle(msg):
    print(msg)
    try:
        userAcc = msg['from']
        msgId = msg['message_id']
        print(userAcc)
    except:
        print()

    if not isContained(userAcc):
        users.append(userAcc)
        print('User added: ' + str(userAcc['id']))

    try:
        if str(msg['text']).__contains__('banna'):
            arr = str(msg['text']).split(" ")
            userToBan = arr[1]

            for u in users:
                for key, value in u.items():
                    if userToBan==value:
                        bot.sendMessage(msg['chat']['id'],'Bye '+value+'! xD',None,None,None,msg['message_id'],None)
                        bot.kickChatMember(msg['chat']['id'], int(u['id']))
                        bot.unbanChatMember(msg['chat']['id'], int(u['id']))
    except:
        print()

bot.message_loop(handle)

def isContained(acc):
    res = False
    for u in users:
        if u['id']==acc['id']:
            res=True
    return res


while 1:
    time.sleep(10)
