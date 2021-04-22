import clientui
from PyQt6 import QtCore, QtGui, QtWidgets
import requests
from datetime import datetime

class ExampleApp(QtWidgets.QMainWindow, clientui.Ui_MainWindow):
    def __init__(self, host='http://127.0.0.1:5000'):
        super().__init__()
        self.setupUi(self)
        self.pushButton.pressed.connect(self.send_message)
        self.host = host
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.get_message)
        self.timer.start(1000)

        self.after = 0

    def show_messages(self, messages):
        for m in messages:
            time_str = datetime.fromtimestamp(m['time'])
            dt = time_str.strftime('%H:%M:%S')
            self.textBrowser.append(f" {dt} {m['name']}:")
            self.textBrowser.append(f'-> {m["text"]}\n')


    def get_message(self):
        try:
            responce = requests.get(f'{self.host}/messeng',
                                 params={'after': self.after, },
                                    )
        except:
            return
        messages = responce.json()['messenger']  # из server.get_mess.
        if len(messages) > 0:
            self.show_messages(messages)
            self.after = messages[-1]['time']

    def send_message(self):
        text = self.textEdit.toPlainText()
        name = self.lineEdit.text()
        try:
            responce = requests.post(f'{self.host}//send',
                                    json={'name': name, 'text': text, },
                                     )
        except:
            self.textBrowser.append(f"serwer not connect")
            return

        # validation
        if responce.status_code != 200:
            self.textBrowser.append(f"Messange uncorrect\nCheck name\n")
            return

        self.textEdit.clear()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    win = ExampleApp()
    win.show()

    app.exec()

    """разверни сервер и запусти месенджер"""