from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

reg_course = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Foundation 🎯", callback_data="regfoun"),
            InlineKeyboardButton(text="Telegram Bot 🤖", callback_data="regbot"),
        ],
        [
            InlineKeyboardButton(text="Python Backend 🦾", callback_data="regback"),
        ]
    ],
)


reg_course_types = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="👤Individual", callback_data="regindi"),
            InlineKeyboardButton(text="👥Gurux bilan", callback_data="reggur")
        ]
    ]
)