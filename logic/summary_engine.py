from collections import Counter


UPDATE_KEYWORDS = [
    "deadline",
    "meeting",
    "result",
    "results",
    "announcement",
    "schedule",
    "submission",
    "exam",
    "project"
]

ACHIEVEMENT_KEYWORDS = [
    "won",
    "selected",
    "completed",
    "achieved",
    "secured",
    "certified"
]


def generate_summary(messages):

    updates = []
    achievements = []
    user_counter = Counter()

    for msg in messages:

        text = msg["text"].lower()

        user_counter[msg["sender"]] += 1

        if any(word in text for word in UPDATE_KEYWORDS):
            updates.append(msg)

        if any(word in text for word in ACHIEVEMENT_KEYWORDS):
            achievements.append(msg)

    active_users = user_counter.most_common(3)

    return {
        "updates": updates,
        "achievements": achievements,
        "active_users": active_users
    }