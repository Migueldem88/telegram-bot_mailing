from aiogram import Bot, types, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


from utils.db_api.db_gino import db

from data import config
bot = Bot(token = config.bot_token, parse_mode=types.ParseMode.HTML)

#Creamos almacenamiento
storage = MemoryStorage()

#Creamos dispatcher
dp=Dispatcher(bot,storage=storage)

__all__=['bot','storage','dp','db']