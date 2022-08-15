from aiogram import types
from loader import dp

@dp.message_handler(text='Hello')
async def command_hello(message=types.Message):
    await message.answer(f"Hello {message.from_user.full_name}")
