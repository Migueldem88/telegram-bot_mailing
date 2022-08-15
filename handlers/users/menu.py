from loader import dp
from aiogram import types
from aiogram.dispatcher.filters import Command
from keyboard.default import kb_menu

#new message handler, import commands from aiogram dispatcher filters
@dp.message_handler(Command("menu"))
async def menu(message: types.Message):
    await message.answer("Choose a number from menu below",reply_markup=kb_menu)