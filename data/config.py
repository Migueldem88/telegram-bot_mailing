import os
from dotenv import load_dotenv


load_dotenv()
bot_token = str(os.getenv('BOT_TOKEN'))
#print(bot_token)

admins_id = [5174799022]

ip=os.getenv('ip')

PGUSER = str(os.getenv('PGUSER'))
PGPASSWORD = str(os.getenv('PGPASSWORD'))
DATABASE = str(os.getenv('DATABASE'))

POSTGRES_URI= f'postgresql://{PGUSER}:{PGPASSWORD}@{ip}/{DATABASE}'