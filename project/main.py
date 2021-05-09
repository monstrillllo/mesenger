import time
from flask import Flask

db = []


def send_message(name, text):
    """send to bd"""
    db.append({
        'name': name,
        'text': text,
        'time': time.time()
    })


def get_message(after):
    """get from db"""
    filtered_messages = []
    for message in db:
        if message['time'] > after:
            filtered_messages.append(message)
    return filtered_messages[:50]
