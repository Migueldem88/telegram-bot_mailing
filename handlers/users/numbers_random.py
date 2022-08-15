from loader import dp
from aiogram import types
from keyboard.randoms import random_menu
from random import randint,sample


@dp.message_handler(text='additional_functions')
async def show_additional_functions(message: types.Message):
    await message.answer('additional_functions_below',reply_markup=random_menu)

@dp.callback_query_handler(text='random_number')
async def rand_number(call: types.CallbackQuery):
    await call.message.answer(str(randint(0, 9)))

@dp.callback_query_handler(text='random_phrase')
async def rand_phrase(call: types.CallbackQuery):
    await call.message.answer(''.join([chr(randint(97, 122)) for x in range(1,6)]))
