import time

from Dice import Dice
from flask import Flask, request, abort
from sender import sender

app = Flask(__name__)
db = []


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/status")
def status():
    not_sorted_users = []
    for ms in db:
        not_sorted_users.append(ms['name'])
    sorted_users = set(not_sorted_users)
    return {
        'status': True,
        'name': 'My server',
        'time': time.time(),
        'users': len(sorted_users),
        'user_names': str(sorted_users),
        'message': len(not_sorted_users)
    }


@app.route("/send", methods=['POST'])
def send():
    data = request.json
    if not isinstance(data, dict):
        return abort(400)
    if 'name' not in data or 'text' not in data:
        return abort(400)

    name = data['name']
    text = data['text']

    if not isinstance(name, str) or not isinstance(text, str):
        return abort(400)
    if not 0 < len(name) <= 64:
        return abort(400)
    if not 0 < len(text) <= 10000:
        return abort(400)

    db.append({
        'name': name,
        'text': text,
        'time': time.time()
    })
    # Вынести бота в отдельный файл и дополнить функционал
    if text == '/help':
        text_help = """
                    /dice for roll the dices
                    /stat for server statistic
                """
        sender('bot', text_help).send()
    elif text == '/stat':
        text_stat = f'Unique users: {status()["users"]}\nMessages: {status()["message"]}'
        sender('bot', text_stat).send()
    elif text == '/dice':
        rezult = Dice(1).roll()
        text_dice = 'You rolled: ' + str(rezult)
        sender('bot', text_dice).send()

    return {}


@app.route("/messages")
def messages():
    try:
        after = float(request.args['after'])
    except:
        return abort(400)

    filtered_messages = []

    for message in db:
        if message['time'] > after:
            filtered_messages.append(message)

    return {'messages': filtered_messages[:50]}


if __name__ == '__main__':
    app.run()
