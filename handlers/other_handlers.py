from aiogram.types import Message
from lexicon.lexicon import LEXIKON_RU
from aiogram import Router

router: Router = Router()

@router.message()
async def send_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TabError:
        await message.answer(text=LEXIKON_RU['/no_echo'])