from loader import dp
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext
from aiogram import types
from states import register
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from keyboard.default import kb_menu
from filters import IsPrivate

@dp.message_handler(IsPrivate(),Command('register')) ##/register
async def registerr(message: types.Message):
    name = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=f"{message.from_user.first_name}")
            ],
        ],
    resize_keyboard = True
    )
    await message.answer("Hi, you've started registration,\nEnter your name",
                         reply_markup=name)
    await register.test1.set()



@dp.message_handler(state=register.test1)
async def state1(message: types.Message, state:FSMContext):
    #Guardamos en text1 el texto envidado por el usuario
    answer = message.text
    await state.update_data(test1 = answer)
    await message.answer(f"How old are you? ")
    await register.test2.set()

@dp.message_handler(state=register.test2)
async def state2(message: types.Message, state:FSMContext):
    answer = message.text

    await state.update_data(test2 = answer)
    data = await state.get_data()
    name = data.get('test1')
    years = data.get('test2')
    await message.answer(f"Registration successfully completed\n"
                         f"Your name is {name}\n"
                         f"You are {years} old",reply_markup=kb_menu)
    await message.edit_reply_markup(kb_menu)
    await state.finish()