import json
import os

GROUP_FILE = "data/groups.json"


def load_groups():
    if not os.path.exists(GROUP_FILE):
        return []

    with open(GROUP_FILE, "r") as file:
        return json.load(file)


def save_groups(groups):
    with open(GROUP_FILE, "w") as file:
        json.dump(groups, file, indent=4)


def add_group(group_name):
    groups = load_groups()

    if group_name not in groups:
        groups.append(group_name)
        save_groups(groups)