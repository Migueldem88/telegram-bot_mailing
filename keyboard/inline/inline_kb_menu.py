from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_menu = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard = [
                                    [InlineKeyboardButton(text='Message', callback_data='Some message'),
                                    InlineKeyboardButton(text='Link',url = 'www.github.com')],

                                    [
                                    InlineKeyboardButton(text='Alert', callback_data='Alert')],

                                    [
                                        InlineKeyboardButton(text='Change menu buttons', callback_data='Buttons2')],
                                ])