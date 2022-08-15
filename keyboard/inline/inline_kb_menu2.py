from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_menu2 = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard = [
                                    [InlineKeyboardButton(text='Message', callback_data='Some message'),
                                    InlineKeyboardButton(text='Link',url = 'www.github.com')
                                     ]
                                ])
