from aiogram import Router, types, F
from aiogram.filters import Command
from crawler.animespirit import AnimeCrawler

scrap_router = Router()


@scrap_router.message(Command('scrap'))
async def make_order(message: types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Начать парсить", callback_data='scrap')
            ]
        ]
    )
    await message.answer('Хотите начать?', reply_markup=kb)

@scrap_router.callback_query(F.data == 'scrap')
async def scrap(callback: types.CallbackQuery):
    crawler = AnimeCrawler()
    animes = await crawler.get_anime_data()
    for anime in animes:
        await callback.message.answer(anime)


