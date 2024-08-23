from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.types.web_app_info import WebAppInfo

start_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🎓 Kurs haqida ma’lumotlar (Online)')
        ],
        [
            KeyboardButton(text='🧑‍💻 Isroilov Rustamjon'),
            KeyboardButton(text='📰 Web Site', web_app=WebAppInfo(url="https://abruis.uz"))

        ],
        [
            KeyboardButton(text="📝 Kursga ro'yxatdan o'tish"),
        ],


    ],
    resize_keyboard=True
)

user_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🎓 Kurs haqida ma’lumotlar (Online)')
        ],
        [
            KeyboardButton(text='🧑‍💻 Isroilov Rustamjon'),
            KeyboardButton(text='📰 Web Site', web_app=WebAppInfo(url="https://abruis.uz"))

        ],
        [
            KeyboardButton(text="📝 Kursga ro'yxatdan o'tish"),
        ],
        [
            KeyboardButton(text='👥 Users'),
            KeyboardButton(text='📲 Reklama')
        ],


    ],
    resize_keyboard=True
)


contact_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="☎️ Contact yuborish", request_contact=True)
        ]
    ],
    resize_keyboard=True
)