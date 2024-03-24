import asyncio
import logging
from aiogram import Bot

from bot import bot, dp, db
from handlers.start import start_router
from handlers.scrap import scrap_router

async def on_startup(bot: Bot):
    pass


async def main():
    dp.include_router(start_router)
    dp.include_router(scrap_router)
    dp.startup.register(on_startup)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main()),