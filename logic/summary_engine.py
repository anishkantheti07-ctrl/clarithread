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

FUTURE_WORDS = [
    "will",
    "might",
    "hopefully",
    "maybe",
    "probably",
    "soon",
    "trying",
    "attempting"
]


def is_real_achievement(text):

    text = text.lower()

    if any(word in text for word in FUTURE_WORDS):
        return False

    return any(word in text for word in ACHIEVEMENT_KEYWORDS)


def generate_summary(messages):

    updates = []
    achievements = []
    user_counter = Counter()

    for msg in messages:

        text = msg["text"].lower()

        user_counter[msg["sender"]] += 1

        if any(word in text for word in UPDATE_KEYWORDS):
            updates.append(msg)

        if is_real_achievement(text):
            achievements.append(msg)

    active_users = user_counter.most_common(3)

    return {
        "updates": updates,
        "achievements": achievements,
        "active_users": active_users
    }