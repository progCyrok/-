from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

btn_anketa = KeyboardButton("ЗАПОЛНИТЬ АНКЕТУ")
btn_anketa_look = KeyboardButton("ПОСМОТРЕТЬ АНКЕТУ")

hi_menu = ReplyKeyboardMarkup(resize_keyboard=True).row(btn_anketa)
look_menu = ReplyKeyboardMarkup(resize_keyboard=True).row(btn_anketa_look)
