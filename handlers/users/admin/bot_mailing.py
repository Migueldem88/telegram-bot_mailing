from asyncio import sleep

from aiogram import types

#from aiogram.utils.deep_linking import get_start_link
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import dp
from filters import IsPrivate

from utils.db_api import quick_commands as commands
from states import bot_mailing

from data.config import admins_id

@dp.message_handler(IsPrivate(), text='/mailing',chat_id=admins_id)
async def start_mailing(message: types.Message):
    await message.answer(f"Type mailing text")
    #We'll set a mailing text state
    await bot_mailing.text.set()

@dp.message_handler(IsPrivate(),state=bot_mailing.text, chat_id=admins_id)
async def mailing_text(message: types.Message, state:FSMContext):
    answer = message.text
    markup = InlineKeyboardMarkup(row_width=2,
                                  inline_keyboard=[
                                      [
                                          InlineKeyboardButton(text='add a photo',
                                                               callback_data='add_photo'),
                                          InlineKeyboardButton(text='Next',
                                                               callback_data='next'),
                                          InlineKeyboardButton(text='Cancel',
                                                               callback_data='quit'),
                                      ]
                                  ]
                                  )
    await state.update_data(text=answer)
    await message.answer(text=answer, reply_markup=markup)
    await bot_mailing.state.set()

@dp.callback_query_handler(text='next',state=bot_mailing.state, chat_id=admins_id)
async def start(call: types.CallbackQuery,state:FSMContext):
    users = await commands.select_all_users()
    # obtain data and text
    data = await state.get_data()
    text = data.get('text')
    await state.finish()
    # iterate all users and try to send a message
    for user in users:
        try:
            await dp.bot.send_message(chat_id = user.user_id, text=text)
        except Exception:
            await call.message.answer("Error")
    await call.message.answer("Mailing done")

@dp.callback_query_handler(text='add_photo',state=bot_mailing.state, chat_id=admins_id)
async def add_photo(call: types.CallbackQuery):
    await call.message.answer('Send a photo')
    await bot_mailing.photo.set()

@dp.message_handler(IsPrivate(),state=bot_mailing.photo,
                    content_types=types.ContentType.PHOTO, chat_id=admins_id)
async def mailing_photo(message: types.Message, state: FSMContext):
    photo_file_id = message.photo[-1].file_id
    await state.update_data(photo=photo_file_id)
    data = await state.get_data()
    text=data.get('text')
    photo=data.get('photo')
    markup=InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Next',
                                                             callback_data='next'),
                                        InlineKeyboardButton(text='Cancel',
                                                             callback_data='quit'),
                                    ]
                                ])
    await message.answer_photo(photo=photo, caption=text,
                               reply_markup=markup)

@dp.callback_query_handler(text='next',state=bot_mailing.photo, chat_id=admins_id)
async def next(call: types.CallbackQuery, state:FSMContext):
    users=await commands.select_all_users()
    #obtain data,text and photo
    data = await state.get_data()
    text = data.get('text')
    photo = data.get('photo')
    await state.finish()
    #iterate all users and try to send a message
    for user in users:
        try:
            await dp.bot.send_photo(chat_id=user.user_id, photo = photo, caption=text)
            await sleep(0.33)
        except Exception:
            await call.message.answer("Error")
    await call.message.answer("Mailing done")

@dp.message_handler(IsPrivate(),state=bot_mailing.photo, chat_id=admins_id)
async def no_photo(message: types.Message):
    markup=InlineKeyboardMarkup(row_width=2,
                                InlineKeyboard=[
                                    [
                                        InlineKeyboardButton(text='Cancel',
                                                             callback_data='quit')
                                    ]
                                ])
    await message.answer('Send me a photo', reply_markup=markup)


@dp.callback_query_handler(text = 'quit',state=[bot_mailing.text,
                    bot_mailing.photo, bot_mailing.state],chat_id=admins_id)
async def quit(call:types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.answer("Mailing cancelled")





