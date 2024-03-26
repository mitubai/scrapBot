import asyncio
import logging

from bot import bot, dp
from handlers.start import start_router
from handlers.scrap import scrap_router


async def main():
    dp.include_router(start_router)
    dp.include_router(scrap_router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())