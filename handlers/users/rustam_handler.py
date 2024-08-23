from aiogram import types
from keyboards.inline.tarmoqlar_inline import tarmoq_inl, ozm_inl
from keyboards.inline.rustam_inl import rustam_inline
from loader import dp


@dp.message_handler(text="🧑‍💻 Isroilov Rustamjon")
async def bot_start(message: types.Message):
    photo = open('static/image/rustam.jpg', 'rb')
    description = """👨‍🏫 Mentor: Isroilov Rustamjon
🧑‍💻 Kasbi: Python Foundation va Beckend mentor (3-yilik tajriba, 250+ shogirtlar)
⚙️ Texnik ko'nikmalari: Python, Telegram Bot, Django, Django Rest, SQLite, PostgreSQL, Git, GitHub, HTML, CSS, C++, Microsoft Office(Word, Excel, Power Point, Paint, va h.k.lar)
💼 Ish joyti: Isystem IT Academy (2022-hozirgacha)
📍 Yashash manzili: Toshkent shahar
"""
    await message.answer_photo(photo=photo, caption=description, reply_markup=rustam_inline)
    await message.delete()


@dp.callback_query_handler(text="ozmback")
async def bot_start(call: types.CallbackQuery):
    await call.message.delete()
    photo = open('static/image/rustam.jpg', 'rb')
    description = """👨‍🏫 Mentor: Isroilov Rustamjon
🧑‍💻 Kasbi: Python Foundation va Beckend mentor (3-yilik tajriba, 250+ shogirtlar)
⚙️ Texnik ko'nikmalari: Python, Telegram Bot, Django, Django Rest, SQLite, PostgreSQL, Git, GitHub, HTML, CSS, C++, Microsoft Office(Word, Excel, Power Point, Paint, va h.k.lar)
💼 Ish joyti: Isystem IT Academy (2022-hozirgacha)
📍 Yashash manzili: Toshkent shahar
"""
    await call.message.answer_photo(photo=photo, caption=description, reply_markup=rustam_inline)


@dp.callback_query_handler(text='resume')
async def resume(call: types.CallbackQuery):
    await call.message.delete()
    resume = open('static/document/resume.pdf', 'rb')
    await call.message.answer_document(document=resume, reply_markup=ozm_inl)


@dp.callback_query_handler(text='tarmoq')
async def resume(call: types.CallbackQuery):
    await call.message.delete()
    tarmoq = open('static/image/social-network.jpg', 'rb')
    await call.message.answer_photo(photo=tarmoq, reply_markup=tarmoq_inl)
