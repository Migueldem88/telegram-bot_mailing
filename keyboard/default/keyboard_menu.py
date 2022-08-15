from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


kb_menu = ReplyKeyboardMarkup(
    keyboard=[
            [
            KeyboardButton(text='10'),
            KeyboardButton(text='11'),
            ],
            [
            KeyboardButton(text='100'),
            ],
            [
            KeyboardButton(text='Inline Menu'),
            KeyboardButton(text='Subscribe'),
            KeyboardButton(text='Like'),
            ],
            [
            KeyboardButton(text='additional_functions'),
            ]
        ],
        resize_keyboard=True

)