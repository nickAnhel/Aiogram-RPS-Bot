import random

from lexicon.lexicon import LEXICON_RU


# Функция возвращает случайный аыбор бота
def get_bot_choice() -> str:
    return random.choice(['rock', 'paper', 'scissors'])


# Вспомогательная функция преобразует выбор пользователя в понятный программе вид
def _normalize_user_choice(user_choice: str) -> str:
    for key in LEXICON_RU:
        if LEXICON_RU[key] == user_choice:
            return key
    raise Exception


# Функция возвращает победителя игры
def get_winner(user_choice: str, bot_choice: str) -> str:
    user_choice = _normalize_user_choice(user_choice)
    rules: dict[str, str] = {'rock': 'scissors',
                             'scissors': 'paper',
                             'paper': 'rock'}

    if user_choice == bot_choice:
        return 'nobody_won'
    elif rules[user_choice] == bot_choice:
        return 'user_won'
    else:
        return 'bot_won'