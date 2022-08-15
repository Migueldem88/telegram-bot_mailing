
from aiogram import executor
from handlers import dp



async def on_startup(dp):

    import filters
    filters.setup(dp)

    from loader import db
    from utils.db_api.db_gino import on_startup

    print('connection to Postgres SQL')
    await on_startup(dp)

    # print("Delete DB")
    # await db.gino.drop_all()

    print("Table creation")
    await db.gino.create_all()
    print("Ready")

    from utils.notify_admins import on_startup_notify
    await on_startup_notify(dp)
    #This function will send message to all admins which we specify

    from utils.set_bot_commands import set_default_commands
    await set_default_commands(dp)

    print("Bot initialized")

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)