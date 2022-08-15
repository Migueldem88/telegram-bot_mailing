from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from random import randint

random_menu = InlineKeyboardMarkup(row_width=2,
            inline_keyboard = [
                    [
                    InlineKeyboardButton(text='random_number',
                                         callback_data='www.github.com'),
                    InlineKeyboardButton(text='random_phrase',
                                         callback_data='you are fag'),

                    ]
                ])

#str(randint(0, 9))