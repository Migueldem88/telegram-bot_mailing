import telebot
from telebot import types
token = '5381286126:AAGQxgYSLn4TEZtn3U39NaLbWreepAva5BE'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    #two parameters. 1 - to which chat
    #2 text #3 format
    mess = f"Hola, <b>{message.from_user.first_name}" \
           f"{message.from_user.last_name}</b>"
    bot.send_message(message.chat.id, mess, parse_mode='html')

# @bot.message_handler(content_types=['text'])
# def get_user_text(message):
#     if message.text=='как дела?':
#         bot.send_message(message.chat.id, "хорошо", parse_mode='html')
#     elif message.text=='photo':
#         photo = open('capy.jpg', 'rb')
#         bot.send_photo(message.chat.id, photo)
#     elif message.text=='id':
#         bot.send_message(message.chat.id, f"Su ID:{message.from_user.id}", parse_mode='html')
#     else:
#         bot.send_message(message.chat.id, "¡I don't understand you", parse_mode='html')

@bot.message_handler(content_types=['pinned_message','photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Охуенная фотка!')

#Buttons
@bot.message_handler(commands=['website'])
def website(message):
    #Markup - переменная для описания доп. разметкиы
    #types - object to create buttonss
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('visit website', url = 'www.github.com'))
    bot.send_message(message.chat.id, 'Go to website', reply_markup=markup)

@bot.message_handler(commands=['help'])
def website(message):
    # Markup - переменная для описания доп. разметкиы
    # types - object to create buttonss
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    website = types.KeyboardButton('web site')
    start = types.KeyboardButton('Start')
    markup.add(website,start)
    bot.send_message(message.chat.id, 'Go to website', reply_markup=markup)
    #reply markup - прикрепление кнопки, указываем переменную

#постоянная обработка
bot.polling(none_stop=True)