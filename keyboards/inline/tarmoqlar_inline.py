from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

tarmoq_inl = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='LinkedIn', url='https://www.linkedin.com/in/rustamjon-isroilov-9a5876246/'),
            InlineKeyboardButton(text='GitHub', url='https://github.com/isroilovrustam')
        ],
        [
            InlineKeyboardButton(text='Instagram', url='https://www.instagram.com/abruisdev/'),
            InlineKeyboardButton(text='YouTube', url='https://www.youtube.com/@abruisdev')
        ],
        [
            InlineKeyboardButton(text="Telegram orqali bog'lanish 📱", url='https://t.me/abdumalikovichuz')
        ],
        [
            InlineKeyboardButton('Back  ↩️', callback_data='ozmback')
        ]
    ],
)

ozm_inl = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Telegram orqali bog'lanish 📱", url='https://t.me/abdumalikovichuz')
        ],
        [
            InlineKeyboardButton('Back  ↩️', callback_data='ozmback')
        ]
    ]
)

aloqar_inl = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Telegram orqali bog'lanish 📱", url='https://t.me/abdumalikovichuz')
        ],
        [
            InlineKeyboardButton('Back  ↩️', callback_data='backk')
        ]
    ]
)

fonda_aloqar_inl = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Telegram orqali bog'lanish 📱", url='https://t.me/abdumalikovichuz')
        ],
        [
            InlineKeyboardButton('Back 🔙', callback_data='foundationback')
        ]

    ]
)

bot_aloqar_inl = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Telegram orqali bog'lanish 📱", url='https://t.me/abdumalikovichuz')
        ],
        [
            InlineKeyboardButton('Back 🔙', callback_data='botback')
        ]

    ]
)

backend_aloqar_inl = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Telegram orqali bog'lanish 📱", url='https://t.me/abdumalikovichuz')
        ],
        [
            InlineKeyboardButton('Back 🔙', callback_data='backendback')
        ]
    ]
)

mvt_aloqar_inl = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Telegram orqali bog'lanish 📱", url='https://t.me/abdumalikovichuz')
        ],
        [
            InlineKeyboardButton('Back 🔙', callback_data='mvtback')
        ]
    ]
)
