from aiogram import types
from loader import dp

@dp.message_handler(text='10')
async def buttons_test(message: types.Message):
    await message.answer(f"Hi {message.from_user.full_name}\n"
                         f"You've chosen number {message.text}")


@dp.message_handler(text='11')
async def buttons_test(message: types.Message):
    await message.answer(f"Hi {message.from_user.full_name}\n"
                         f"You've chosen number {message.text}")

@dp.message_handler(text='100')
async def buttons_test(message: types.Message):
    await message.answer(f"Hi {message.from_user.full_name}\n"
                         f"You've chosen number {message.text}")