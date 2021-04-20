from flask import Flask, json, request, abort
from datetime import datetime
import time

app = Flask(__name__)
db =[
     {'name':'Waal',
           'text':'soski',
           'time':time.time(),},

     {'name':'Lessi',
           'text':'Lox',
           'time':time.time(),},
     ]


@app.route('/')
def hi():
    return ('Hello world!')


@app.route('/status')
def status():
    dt = datetime.now()
    json_status = json.dumps(
        {'status': True,
         'name': "DeadMessenger",
         'time': time.time(),
         'time2': dt,
         'time3': dt.isoformat(),
         'time4': dt.strftime('%d %b %Y %H:%M'),
        }
    )
    return json_status


@app.route('/send', methods=['POST'])
def send_mess():
    data = request.json
    # validation
    if not isinstance(data, dict):
        return abort(400)       # return error

    if 'name' not in data and 'text' not in data:
         return abort(400)

    name = data['name']
    text = data['text']

    if not isinstance(name, str) or not isinstance(text, str):
        return abort(400)

    if name == '' or text == '':
        return abort(400)

    message = {'name': name,
               'text': text,
               'time': time.time(),
               }
    db.append(message)
    return {'ok':True}

# get messages
@app.route('/messeng')
def get_mess():
    try:
        after = float(request.args['after'])
    except:
        return abort(400)

    mess = []
    for m in db:
        if m['time'] > after:
            mess.append(m)
    return {'messenger': mess[:20]}


if __name__ == '__main__':
    app.run(port=5000)
