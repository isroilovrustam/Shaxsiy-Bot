import json
import time

from aiogram import types
import requests
from aiogram.dispatcher import FSMContext
from data.config import API, ADMINS
from keyboards.inline.rustam_inl import ha_yoq
from loader import dp, bot
from aiogram.utils import exceptions as aiogram_exceptions
from states.person import ReklamaState
from keyboards.inline.subscription_inline import delete_text


@dp.message_handler(text="👥 Users", user_id=ADMINS)
async def all_users(message: types.Message):
    users = requests.get(url=f"{API}/users/")
    text = f"Users: {len(users.json())}\n"

    for i in users.json():
        text += f"Id: {i['id']}\n"
        text += f"🧑‍💼Name: {i['name']}\n"
        text += f"🆔Chat id: {i['chat_id']}\n"
        if i["id"] % 40 == 0:
            await message.answer(text, reply_markup=delete_text)
            text = f"Users: {len(users.json())}\n"
    await message.answer(text, reply_markup=delete_text)


@dp.message_handler(text='📲 Reklama', user_id=ADMINS)
async def enter_test(message: types.Message):
    await message.answer(f"Salom {message.from_user.full_name} Reklamani yuborishni hohlaysizmi ⁉️",
                         reply_markup=ha_yoq)


@dp.callback_query_handler(text='yoq', user_id=ADMINS)
async def hsa(call: types.CallbackQuery):
    await call.message.answer("Reklama yuborish to'xtatildi!!!")
    await call.message.delete()


@dp.callback_query_handler(text='ha', user_id=ADMINS)
async def hsa(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Reklamani yuboring ❗")
    await ReklamaState.message.set()


@dp.message_handler(state=ReklamaState.message,
                    content_types=[types.ContentType.VIDEO_NOTE, types.ContentType.TEXT, types.ContentType.PHOTO,
                                   types.ContentType.VIDEO])
async def bot_start(message: types.Message, state: FSMContext):
    users = requests.get(url=f"{API}/users/")
    await state.finish()
    if users.status_code == 200:
        try:
            if message.video_note:
                data = message.video_note.file_id
                for user in users.json():
                    user_id = user["chat_id"]
                    try:
                        await bot.send_video_note(chat_id=user_id, video_note=data)
                    except aiogram_exceptions.BotBlocked:
                        pass
                    time.sleep(1)

            elif message.photo:
                data = message.photo[-1].file_id  # Eng yuqori sifatli rasmni olish
                caption = message.caption if message.caption else ""
                for user in users.json():
                    user_id = user["chat_id"]
                    try:
                        await bot.send_photo(chat_id=user_id, photo=data, caption=caption)
                    except aiogram_exceptions.BotBlocked:
                        pass
                    time.sleep(1)

            elif message.video:
                data = message.video.file_id
                caption = message.caption if message.caption else ""
                for user in users.json():
                    user_id = user["chat_id"]
                    try:
                        await bot.send_video(chat_id=user_id, video=data, caption=caption)
                    except aiogram_exceptions.BotBlocked:
                        pass
                    time.sleep(1)

            elif message.text:
                data = message.text
                for user in users.json():
                    user_id = user["chat_id"]
                    try:
                        await bot.send_message(chat_id=user_id, text=data)
                    except aiogram_exceptions.BotBlocked:
                        pass
                    time.sleep(1)
        except:
            pass

    else:
        await message.answer("Foydalanuvchilarni olishda xatolik yuz berdi.")
