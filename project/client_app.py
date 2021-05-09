from datetime import datetime
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer
from sender import sender
from receiver import receiver

import client_ui


class Client_App(QtWidgets.QMainWindow, client_ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.name = ''
        self.text = ''
        self.receiver = receiver()
        self.pushButton.clicked.connect(self.send_message)
        self.pushButton.setAutoDefault(True)
        self.textEdit.setFocus()
        self.timer = QTimer()
        self.timer.timeout.connect(self.get_messages)
        self.timer.start(1000)

    def send_message(self):
        self.name = self.lineEdit_2.text()
        self.text = self.textEdit.toPlainText()
        sender(self.name, self.text).send()

    def get_messages(self):
        messages = self.receiver.get_messages()
        if messages:
            for message in messages:
                decorated_message = str(datetime.fromtimestamp(message['time']).strftime('%H:%M:%S')) + ' ' \
                                                                                                        ' ' + message[
                                        'name'] + ': ' + '\n ' + message['text']
                self.textBrowser.append(decorated_message)
                self.textEdit.clear()
        else:
            return


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Client_App()
    window.show()
    app.exec()
