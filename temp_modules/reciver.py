import requests
from datetime import datetime
import time


def print_messages(mess):
    for m in mess:
        time_str = datetime.fromtimestamp(m['time'])
        dt = time_str.strftime('%H:%M')
        print(f" {dt} {m['name']}:")
        print('->', m['text'])


after = 0
n = 0
while True:
    responce = requests.get('http://127.0.0.1:5000/messeng',
                             params={'after': after, }, )
    messages = responce.json()['messenger']  # из server.get_mess.
    # print_messages(messages)
    if len(messages) > 0:
        print_messages(messages)
        after = messages[-1]['time']
    time.sleep(2)
