import json

from aiogram import types
import requests
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery

from data.config import CHANNELS, API
from filters import IsPrivate
from keyboards.default.start_keyboard import start_btn, user_btn
from keyboards.inline.subscription_inline import check_button
from loader import dp
from utils.misc import subscription


@dp.message_handler(IsPrivate(), CommandStart())
async def bot_start(message: types.Message):
    r = requests.get(url=f"{API}/user/{message.from_user.id}")
    if r.status_code == 404:
        r = requests.post(url=f"{API}/users", data=json.dumps({"chat_id": str(message.from_user.id),
                                                               "name": f"{message.from_user.first_name} {message.from_user.last_name}"}))
    if message.from_user.id == 1913259929:
        await message.answer(f"Assalomu alykum, Admin - {message.from_user.full_name}!", reply_markup=user_btn)
    else:
        await message.answer(f"Assalomu alykum, {message.from_user.full_name}!", reply_markup=start_btn)


@dp.callback_query_handler(text="check_subs")
async def checker(call: types.CallbackQuery):
    await call.answer()
    result = str()
    for channel in CHANNELS:
        status = await subscription.check(user_id=call.from_user.id,
                                          channel=channel)
        if status:
            await call.message.delete()
            result += (f"Yaxshi, {call.from_user.full_name} foydalanishingiz mumkin👇🏻")
            await call.message.answer(result, disable_web_page_preview=True, reply_markup=start_btn)
        else:
            await call.message.delete()
            result += (
                f"🚫Obuna bo'lmadingiz, qayta urinib ko'ring\n\n♻️Kanalga obuna bo'lib \"🔄 Obunani tekshirish\" ni bosing")
            await call.message.answer(result, disable_web_page_preview=True, reply_markup=check_button)


@dp.callback_query_handler(text="karzinka")
async def kar(call: CallbackQuery):
    await call.message.delete()

