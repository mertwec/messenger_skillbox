import requests

name = input('your name: ')
while True:
    responce = requests.post('http://127.0.0.1:5000/send',
                             json={'name': name,
                                   'text': input('text: '), },
                             )


# print(f'{responce.json()}')
