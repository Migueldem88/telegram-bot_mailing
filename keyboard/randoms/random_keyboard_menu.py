from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from random import randint

random_menu = InlineKeyboardMarkup(row_width=2,
            inline_keyboard = [
                    [
                    InlineKeyboardButton(text='random_number',
                                         callback_data='random_number'),
                    InlineKeyboardButton(text='random_phrase',
                                         callback_data='random_phrase'),

                    ]
                ])

#str(randint(0, 9))