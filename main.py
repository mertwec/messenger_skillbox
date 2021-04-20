# -*- coding: utf-8 -*-

#import numpy as np
#import flask

from datetime import datetime
from time import time
# database
db =[
     {'name':'Waal',
           'text':'soski',
           'time':time(),},

     {'name':'Lessi',
           'text':'Lox',
           'time':time(),},
     ]

def print_messages(mess):
    for m in mess:
        time_str= datetime.fromtimestamp(m['time'])
        print(f"{m['name']}, {time_str}")
        print('->', m['text'],'\n')

# send = put messenge into DB
def send_mess(name, text):
    message = {'name':name,
               'text':text,
               'time':time(),
               }
    db.append(message)

# get messages
def get_mess(after):
    mess = []
    for m in db:
        if m['time'] > after:
            mess.append(m)
    return mess[:10]


if __name__ == '__main__':
    result = get_mess(0)
    print_messages(result)
    last_time = result[-1]['time']
    print(f'---lasttime = {last_time}\n')

    send_mess('July', 'hello loshki')

    result = get_mess(last_time)
    print_messages(result)
    last_time = result[-1]['time']

    send_mess('Waal', 'go troinichok')
    send_mess('lilu', 'yiiiiiiiii')

    result = get_mess(last_time)
    print_messages(result)
    last_time = result[-1]['time']
    print(f'----lasttime = {last_time}\n')
    # print(get_mess(0))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
