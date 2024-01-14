from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon import LEXICON_RU


# Клавиатура Отказа и Согласия (через ReplyMarkupBuilder)

# Кнопки согласия и отказа
button_yes: KeyboardButton = KeyboardButton(text=LEXICON_RU['yes_button'])
button_no: KeyboardButton = KeyboardButton(text=LEXICON_RU['no_button'])

# Инициализируем билдер
yes_no_kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

# Добавляем кнопки в билдер
yes_no_kb_builder.row(button_yes, button_no, width=2)

# Создаем икземпляр клавиатуры
yes_no_keyboard: ReplyKeyboardMarkup = yes_no_kb_builder.as_markup(one_time_keyboard=True,
                                                                   resize_keyboard=True)


# Игровая клавиатура (без билдера)

# Кнопки камень, ножницы и бумага
button_rock: KeyboardButton = KeyboardButton(text=LEXICON_RU['rock'])
button_paper: KeyboardButton = KeyboardButton(text=LEXICON_RU['paper'])
button_scissors: KeyboardButton = KeyboardButton(text=LEXICON_RU['scissors'])

# Создаем экземпляр игровой клавитуры
game_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[button_rock],
                                                                   [button_scissors],
                                                                   [button_paper]],
                                                        resize_keyboard=True)