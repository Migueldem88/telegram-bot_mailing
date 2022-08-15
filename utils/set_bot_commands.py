from aiogram import types

async def set_default_commands(dp):
    #Command (name of command, its description)
    await dp.bot.set_my_commands([
        types.BotCommand('start','Initialize bot'),
        types.BotCommand('help', 'Help'),
        types.BotCommand('profile','Get data from DB'),
        types.BotCommand('register','register')
    ])