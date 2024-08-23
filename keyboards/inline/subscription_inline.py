from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

check_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Obuna bo'lish", url='https://t.me/abruis_code')
        ],
        [
            InlineKeyboardButton(text="🔄 Obunani tekshirish", callback_data="check_subs")
        ]
    ]
)


delete_text = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('🗑', callback_data="karzinka")
        ]
    ]
)