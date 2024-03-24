from aiogram import Router, F, types
from aiogram.filters import Command
import logging



start_router = Router()


@start_router.message(Command("start"))
async def start(message: types.Message):
    logging.info(message.from_user)
    await message.answer(f"Hello, {message.from_user.first_name}\n"
                         f"/scrap - парсинг",)


@start_router.callback_query(F.data == "about")
async def about(callback: types.CallbackQuery):
    await callback.message.answer("О нас:")


