from aiogram import types
#from aiogram.types import user
from aiogram.dispatcher.filters import CommandStart
from loader import dp

from filters import IsPrivate
from utils.db_api import quick_commands as commands
from utils.db_api.schemes.user import User

@dp.message_handler(IsPrivate(), CommandStart())
async def command_start(message: types.Message):
    args=message.get_args()#start 123
    print(args)
    new_args = await commands.check_args(args, message.from_user.id)
    print(new_args)
    try:
        user = await commands.select_user(message.from_user.id)
        #Check for ban
        if user.status == 'active':
            await message.answer(f"Hi {user.first_name}\n"
                         f"Your are already signed in")
        elif user.status == 'banned':
            await message.answer("You are banned")
    except Exception:
        await commands.add_user(user_id=message.from_user.id,
                                first_name=message.from_user.first_name,
                                last_name=message.from_user.last_name,
                                username=message.from_user.username,
                                referral_id=int(new_args),
                                status='active',
                                balance=0)
        try:
            await dp.bot.send_message(chat_id=int(new_args),
                                      text=f"{message.from_user.first_name} registered"
                                           f"using your link")
        except Exception:
            pass
        await message.answer("You are successfully registered")

@dp.message_handler(IsPrivate(), text='/ban')
async def get_ban(message: types.Message):
    await commands.update_status(user_id=message.from_user.id, status='banned')
    await message.answer('You ve been banned')

@dp.message_handler(IsPrivate(), text='/unban')
async def get_ban(message: types.Message):
    await commands.update_status(user_id=message.from_user.id, status='active')
    await message.answer('You ve been unbanned')

@dp.message_handler(IsPrivate(), text='/profile')
async def get_profile(message: types.Message):
    user = await commands.select_user(message.from_user.id)
    await message.answer(f"ID - {user.user_id}\n"
                         f"first_name - {user.first_name}\n"
                         f"last_name - {user.last_name}\n"
                         f"username - {user.username}\n"
                         f"status - {user.status}")