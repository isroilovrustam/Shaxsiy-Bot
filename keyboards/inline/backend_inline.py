from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

course_inl = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Foundation 🎯", callback_data='foundation')
        ],
        [
            InlineKeyboardButton(text="Telegram Bot 🤖", callback_data='bot')
        ],
        [
            InlineKeyboardButton(text='Python Backend 🦾', callback_data='backend')
        ],
        [
            InlineKeyboardButton(text='Kerakli noutbuk 💻', callback_data='noutbuk'),
        ],
        [
            InlineKeyboardButton('🗑', callback_data="karzinka")
        ]
    ],
    resize_keyboard=True
)

beck_inl = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='1', callback_data='1b'),
            InlineKeyboardButton(text='2', callback_data='2b'),
            InlineKeyboardButton(text='3', callback_data='3b'),
        ],
        [
            InlineKeyboardButton(text="Telegram orqali bog'lanish 📱", url='https://t.me/abdumalikovichuz')
        ],
        [
            InlineKeyboardButton('Back 🔙', callback_data='backendback')
        ]
    ]
)
