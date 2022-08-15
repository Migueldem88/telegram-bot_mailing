import asyncio

from data import config
from utils.db_api import quick_commands as commands
from utils.db_api.db_gino import db


async def db_test():
    await db.set_bind(config.POSTGRES_URI)
    #Delete all the tables we have
    #await db.gino.drop_all()
    await db.gino.create_all()

    #Create new users:
    await commands.add_user(1,'Miguel','Net')
    await commands.add_user(2,'Carpincho', 'Some name')
    await commands.add_user(3, 'Fenneck','f3')
    await commands.add_user(345254, 'grk', 'rgrg')
    await commands.add_user(454, 'Frgrk', 'fy6')

    users = await commands.select_all_users()
    print(users)

    count = await commands.count_users()
    print(count)

    user = await commands.select_user(1)
    print(user)

    await commands.update_user_name(454, "Boris")

    user = await commands.select_user(1)
    print(user)

loop = asyncio.get_event_loop()
loop.run_until_complete(db_test())