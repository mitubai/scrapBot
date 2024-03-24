from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from os import getenv
from db.base import Database


load_dotenv()
bot = Bot(token=getenv("BOT_TOKEN"))
dp = Dispatcher()
db = Database()