from loader import dp
from aiogram import types
from keyboard.inline import ikb_menu,ikb_menu2
from keyboard.default import kb_test


@dp.message_handler(text='Inline Menu')
async def show_inline_menu(message: types.Message):
    await message.answer('Inline buttons below',reply_markup=ikb_menu)

@dp.callback_query_handler(text='Some message')
async def send_message(call: types.CallbackQuery):
    await call.message.answer('Buttons changed',reply_markup=kb_test)

@dp.callback_query_handler(text='Alert')
async def send_message(call: types.CallbackQuery):
    await call.answer('Buttons changed', show_alert=True)

@dp.callback_query_handler(text='Buttons2')
async def send_message(call: types.CallbackQuery):
    await call.message.edit_reply_markup(ikb_menu2)