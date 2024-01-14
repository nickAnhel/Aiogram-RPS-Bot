from aiogram import Router
from aiogram.types import Message

from lexicon.lexicon import LEXICON_RU


router: Router = Router()

# Хэндлер обработки сообщений, не прошедших другие хэндлеры
@router.message()
async def process_other_message(message: Message):
    await message.answer(text=LEXICON_RU['other_answer'])