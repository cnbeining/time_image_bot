#! /usr/bin/python3

import datetime
import time
import os
import pprint
import telepot
from telepot.loop import MessageLoop

# print = pprint.PrettyPrinter().pprint

def doit(chat_id):
    temp = " 已經\n "
    
    temp += datetime.datetime.now().strftime("%H:%M")
    
    temp += "\n 了!!\n"
    
    print (temp)
    
    with open('temp.txt', 'w') as fout:
        fout.write(temp)
        
    os.system('soffice --convert-to jpg temp.txt')
    os.system('convert temp.jpg -crop 125x300+50+0 temp.jpg')
    os.system('convert temp.jpg -resize 200% temp.jpg')
    os.system('convert temp.jpg -crop 125x300+40+50 temp.jpg')
    os.system('montage temp.jpg bot.jpg -tile 1x2 -geometry +0+0 temp.jpg')
    os.system('montage left.jpg temp.jpg -tile 2x1 -geometry +0+0 temp.jpg')

    fout = open('temp.jpg', 'rb')
    print ('sending photo...')
    bot.sendPhoto(chat_id, fout)


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    # print ('Content type: %s' % content_type)
    print (content_type, chat_type, chat_id)

    if chat_type == 'private': doit(chat_id)
    elif content_type == 'text' and '@time_image_bot' in msg['text']:
        doit(chat_id)
    

bot = telepot.Bot('')

MessageLoop(bot, handle).run_as_thread()
print ('I am listening ...')

while 1:
    time.sleep(10)
