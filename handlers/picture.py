import random

from aiogram import Router, types
from aiogram.filters import Command
import logging
from pathlib import Path


picture_router = Router()


@picture_router.message(Command("pic"))
async def send_pic(message: types.Message):
    file_name = random.choice(list((Path(__file__).parent.parent/"images").iterdir()))
    file_path = Path(__file__).parent.parent / "images" / file_name
    logging.info(file_path)
    file = types.FSInputFile(file_path)
    await message.answer_photo(file)