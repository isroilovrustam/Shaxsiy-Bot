from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

foundation_inl = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Ochiq dars 🎥', callback_data='foundationochiq')
        ],
        [
            InlineKeyboardButton(text='Kurs davomida 👨‍🏫', callback_data='fokursdavomida'),
            InlineKeyboardButton(text="Pythonni o'rnatish 📥", callback_data='pythonornat')
        ],
        [
            InlineKeyboardButton(text='Misollar 📝', callback_data='misollar')
        ],
        [
            InlineKeyboardButton('Back  ↩️', callback_data='backk')
        ]
    ]
)

bot_inl = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Ochiq dars 📹', callback_data='boochiqdars')
        ],
        [
            InlineKeyboardButton(text='Kurs davomida 👨‍🏫', callback_data='bokursdavomida'),
            InlineKeyboardButton(text='Bot Shablon 🗂', callback_data='botshablon')
        ],
        [
            InlineKeyboardButton('Back  ↩️', callback_data='backk')
        ]
    ],
)

backend_inl = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Ochiq dars 📽', callback_data='beochiqdars')
        ],
        [
            InlineKeyboardButton(text='Kurs davomida 👨‍🏫', callback_data='bekursdavomida'),
            InlineKeyboardButton(text='MVT Shablon 🗂', callback_data='mvtshablon')
        ],
        [
            InlineKeyboardButton('Back  ↩️', callback_data='backk')
        ]
    ],
    resize_keyboard=True
)

misolar_inl = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='1', callback_data='1'),
            InlineKeyboardButton(text='2', callback_data='2'),
            InlineKeyboardButton(text='3', callback_data='3'),
        ],
        [
            InlineKeyboardButton(text='4', callback_data='4'),
            InlineKeyboardButton(text='5', callback_data='5'),
            InlineKeyboardButton(text='6', callback_data='6'),
        ],
        [
            InlineKeyboardButton(text='7', callback_data='7'),
            InlineKeyboardButton(text='8', callback_data='8'),
            InlineKeyboardButton(text='9', callback_data='9'),
        ],
        [
            InlineKeyboardButton(text='10', callback_data='10'),
            InlineKeyboardButton(text='11', callback_data='11'),
        ],
        [
            InlineKeyboardButton(text='12 (LeetCode)', url='https://leetcode.com/'),
        ],
        [
            InlineKeyboardButton('Back 🔙', callback_data='foundationback')
        ]
    ]
)

ortga_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('📝 Mavzularga qaytish', callback_data='qaytish')
        ]
    ]
)
