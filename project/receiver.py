import time
from datetime import datetime

import requests


class receiver:

    def __init__(self):
        self.after = 0
        self.messages = []

    def get_messages(self):
        try:
            response = requests.get(
                'https://6c4755808100.ngrok.io/messages',
                params={'after': self.after}
            )
            self.messages = response.json()['messages']

            if self.messages:
                self.after = self.messages[-1]['time']
                return self.messages
        except:
            return
