from aiogram import types
from loader import dp
from filters import IsPrivate


@dp.message_handler(IsPrivate(), text='/start')
async def common_start(message=types.Message):
    await message.answer(f"Hi {message.from_user.full_name}\n"
                         f"Your id is {message.from_user.id}")