from asyncpg import UniqueViolationError
from utils.db_api.db_gino import db
from utils.db_api.schemes.user import User


#Here we add data from user.py

async def add_user(user_id : int, first_name : str,
                   last_name : str, username: str, referral_id:int, status:str,
                   balance: float):
    try:
        user = User(user_id=user_id,first_name=first_name,
                    last_name = last_name, username=username,
                    referral_id=referral_id, status=status,
                    balance=balance)
        await user.create()
    except UniqueViolationError:
        print("User not added")

#Gets all users from DB
async def select_all_users():
    users = await User.query.gino.all()
    return users

async def count_users():
    count=await db.func.count(User.user_id).gino.scalar()
    return count

#Selects a certain USER by user_id
async def select_user(user_id):
    user = await User.query.where(User.user_id==user_id).gino.first()
    return user

#Updates username
async def update_status(user_id, status):
    user = await select_user(user_id)
    await user.update(status=status).apply()

async def count_refs(user_id):
    refs = await User.query.where(User.referral_id==user_id).gino.all()
    return len(refs)

async def check_args(args, user_id:int):
    #If row is empty:
    if args=='':
        args = '0'
        return args
    #If the arg has not only numbers, but also letters
    elif not args.isnumeric():
        args='0'
        return args
    #If the arg contains only numbers
    elif args.isnumeric():
        #if the arg is the same as user's ID
        if int(args)==user_id:
            args='0'
            return args
        #We get from DB a suer with ID the same as passed argument
        elif await select_user(user_id=int(args)) is None:
            args='0'
            return args
        #if our arg passed all the checks we return it
        else:
            args=str(args)
            return args
    #if something went wrong:
    else:
        args='0'
        return args

#the function to change balance
async def change_balance(user_id:int, amount):
    user = await select_user(user_id)
    new_balance=user.balance+amount
    await user.update(balance=new_balance).apply()

#the function to check balance
async def check_balance(user_id:int, amount):
    user = await select_user(user_id=user_id)
    try:
        amount = float(amount)
        if user.balance + amount >= 0:
            await change_balance(user_id, amount)
            return True
        elif user.balance + amount < 0:
            return 'no money'
    except Exception:
        return False


