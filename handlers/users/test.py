from aiogram import types
from loader import dp
from keyboard.default import kb_test

@dp.message_handler(text='any_text')
async def test(message=types.Message):
    await message.answer(f"Hi {message.from_user.full_name}\n"
                         f"Here should be some text", reply_markup=kb_test)