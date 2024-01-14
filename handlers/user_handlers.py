from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command, Text

from keyboards.keyboards import game_keyboard, yes_no_keyboard
from lexicon.lexicon import LEXICON_RU
from services.services import get_bot_choice, get_winner


router: Router = Router()


# Хэндлер обрабатывает команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=yes_no_keyboard)


# Хэндлер обрабатывает команду /help
@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'], reply_markup=yes_no_keyboard)


# Хэндлер обрабатывает согласие на игру
@router.message(Text(text=LEXICON_RU['yes_button']))
async def process_yes_answer(message: Message):
    await message.answer(text=LEXICON_RU['yes'], reply_markup=game_keyboard)


# Хэндлер обрабатывает отказ от игры
@router.message(Text(text=LEXICON_RU['no_button']))
async def process_no_answer(message: Message):
    await message.answer(text=LEXICON_RU['no'])


# Хэндлер обрабатывает выбор пользователя в игре
@router.message(Text(text=[LEXICON_RU['rock'], LEXICON_RU['paper'], LEXICON_RU['scissors']]))
async def process_game_choice(message: Message):
    bot_choice = get_bot_choice()
    await message.answer(text=f'{LEXICON_RU["bot_choice"]} - {LEXICON_RU[bot_choice]}')

    winner = get_winner(message.text, bot_choice)
    await message.answer(text=LEXICON_RU[winner], reply_markup=yes_no_keyboard)