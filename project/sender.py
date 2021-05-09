import requests


class sender:

    def __init__(self, name, text):
        self.name = name
        self.text = text
        self.data = {
            'name': self.name,
            'text': self.text
        }

    def send(self):
        try:
            requests.post('https://6c4755808100.ngrok.io/send', json=self.data)
        except:
            return
