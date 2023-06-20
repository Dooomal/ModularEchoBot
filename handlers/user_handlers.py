from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from lexicon.lexicon import LEXIKON_RU
from aiogram import Router

router: Router = Router()

@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXIKON_RU['/start'])

@router.message(Command(commands='/help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXIKON_RU['/help'])

