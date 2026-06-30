import json
import os
from datetime import datetime

MESSAGE_FILE = "data/messages.json"


def load_messages():
    if not os.path.exists(MESSAGE_FILE):
        return {}

    with open(MESSAGE_FILE, "r") as file:
        return json.load(file)


def save_messages(messages):
    with open(MESSAGE_FILE, "w") as file:
        json.dump(messages, file, indent=4)


def add_message(group_name, sender, text):
    messages = load_messages()

    if group_name not in messages:
        messages[group_name] = []

    messages[group_name].append({
        "sender": sender,
        "text": text,
        "timestamp": datetime.now().strftime("%d-%m-%Y %H:%M")
    })

    save_messages(messages)


def get_group_messages(group_name):
    messages = load_messages()
    return messages.get(group_name, [])