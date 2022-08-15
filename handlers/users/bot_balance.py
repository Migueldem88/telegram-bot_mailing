from aiogram import types

#from aiogram.utils.deep_linking import get_start_link
from aiogram.dispatcher import FSMContext
from loader import dp
from filters import IsPrivate
from states import balance
from utils.db_api import quick_commands as commands

@dp.message_handler(IsPrivate(), text='/balance')
async def change_balance(message: types.Message):
    user= await commands.select_user(message.from_user.id)
    await message.answer(f"Balance - {user.balance}")

@dp.message_handler(IsPrivate(), text='/change_balance')
async def change_balance(message: types.Message):
    await message.answer("Enter the top up amount: ")
    await balance.amount.set()

@dp.message_handler(IsPrivate(), state=balance.amount)
async def change_balance(message: types.Message, state: FSMContext):
    answer = message.text
    check_balance = await commands.check_balance(user_id = message.from_user.id,
                                                 amount=answer)
    if check_balance == 'no money':
        await message.answer("Insufficient funds")
        await state.finish()
    elif check_balance:
        await message.answer('Balance successfully changed')
        await state.finish()
    elif not check_balance:
        await message.answer('wrong number')
        await state.finish()
    else:
        await message.answer('Error. Use command /start')
        await state.finish()