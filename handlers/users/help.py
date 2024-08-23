from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("""🤖 Yordam kerak bo'lsa 
🧑‍💻 Adminga murojar qiling! 
http://t.me/abdumalikovichuz""")
    
    await message.answer(text)
