from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

rustam_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Resume 📝", callback_data='resume')
        ],
        [
            InlineKeyboardButton(text='Ijtimoiy tarmoqlar 🌍', callback_data='tarmoq')
        ],
        [
            InlineKeyboardButton(text="Telegram orqali bog'lanish 📱", url='https://t.me/abdumalikovichuz')
        ],
        [
            InlineKeyboardButton('🗑', callback_data="karzinka")
        ]
    ],
    resize_keyboard=True
)

ha_yoq = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("✅ Ha", callback_data='ha'),
            InlineKeyboardButton("🚫 Yoq", callback_data='yoq')
        ]
    ]
)

ha_yoq_register = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("✅ Ha", callback_data='har'),
            InlineKeyboardButton("🚫 Yoq", callback_data='yoqr')
        ]
    ]
)

ha_yoq_tasdiq = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("✅ Ha", callback_data='hat'),
            InlineKeyboardButton("🚫 Yoq", callback_data='yoqt')
        ]
    ]
)

inline_mode_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🚀 Start Bot", url='https://t.me/abruisbot')
        ]
    ]
)
