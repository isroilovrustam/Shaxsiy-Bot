import os

from aiogram import types

from keyboards.inline.misolar_inline import backend_inl
from keyboards.inline.tarmoqlar_inline import backend_aloqar_inl, mvt_aloqar_inl
from keyboards.inline.backend_inline import beck_inl
from loader import dp, bot


@dp.callback_query_handler(text='beochiqdars')
async def bot_found(call: types.CallbackQuery):
    await call.message.delete()
    text = '📽 Python Beckend ochiq dars video tayorlanmoqda tez orada botga joylanadi...'
    await call.message.answer(text, reply_markup=backend_aloqar_inl)


@dp.callback_query_handler(text='bekursdavomida')
async def bot_found(call: types.CallbackQuery):
    await call.message.delete()
    img = open('static/image/pythonback.jpg', 'rb')
    text = """💻  Kursing davomiyligi 5 oy bo’lib, haftada 3 kun 2 soat dan bo’lib o’tadi. Kurs davomida siz:

— Internet infrastrukturasi protokollar haqida tushuncha;
— Sof SQL bilan ishlash va murakkab so'rovlarni optimallashtirish;
— Fayllarni server va databasega saqlash va olish;
— Django web framework arxitekturasi ishlash mexanizmi;
— MVT da sayt yoza olish
— API ishlab chiqish, uchinchi tomon xizmatlari bilan integratsiya;
— Dokumentatsiya yaratish va undan foydalansh;
— Web texlogiyalari va ularning ishlash mexanizmi;
— Rest full api yoza olish;
— Konteynerlash texnologiyalari, Deploy qilish;
— Python web frameworklari afzalliklari va kamchiliklar;
 
💸 Kurslarning narxiga keladigan bo'lsak

🔰 Oldindan oyiga to’lov:
   👤 Individual 1 500 000  so'm.
   👥 Gurux bilan 8 000 000 so'm"""

    await call.message.answer_photo(photo=img, caption=text, reply_markup=backend_aloqar_inl)


@dp.callback_query_handler(text='mvtshablon')
async def bot_found(call: types.CallbackQuery):
    await call.message.delete()
    img = open('static/image/front.jpg', 'rb')
    text = '🗂 <b>Web sayt shablonlari</b>\n\n'
    text += "1 - Resume sayt\n"
    text += "2 - Blog sayt\n"
    text += "3 - eCommerce sayt\n"
    await call.message.answer_photo(photo=img, caption=text, reply_markup=beck_inl)


@dp.callback_query_handler(text='mvtback')
async def bot_found(call: types.CallbackQuery):
    await call.message.delete()
    img = open('static/image/front.jpg', 'rb')
    text = '🗂 <b>Web sayt shablonlari</b>\n\n'
    text += "1 - Resume sayt\n"
    text += "2 - Blog sayt\n"
    text += "3 - eCommerce sayt\n"
    await call.message.answer_photo(photo=img, caption=text, reply_markup=beck_inl)


@dp.callback_query_handler(text='backendback')
async def bot_found(call: types.CallbackQuery):
    await call.message.delete()
    text = """📌 Backend Python  dasturlash tili veb-ilovalar va boshqa dasturiy tizimlarning orqa qismini yaratish va boshqarish uchun ishlatiladigan dasturiy ta'minotni ishlab chiqishni anglatadi.

👨🏻‍💻 Python backend-bu mijoz tomoni (frontend) so'rovlarini ko'rib chiqadigan va ma'lumotlar bazalari bilan o'zaro aloqada bo'lgan, biznes mantig'ini bajaradigan, xavfsizlik, ma'lumotlarni qayta ishlash va boshqa funktsiyalarni ta'minlaydigan dasturlarning server tomoni.

🐍 Python backend dasturlarini ishlab chiqishni osonlashtiradigan ko'plab kutubxonalar va ramkalarni taklif etadi. Backend rivojlanishi uchun ba'zi mashhur Python ramkalariga Django, Flask, Pyramid va Bottle kiradi. Ular marshrutlarni boshqarish, ma'lumotlar bazalari bilan ishlash, API ishlab chiqish va backend ishlab chiqish uchun zarur bo'lgan boshqa vazifalar uchun qulay vositalarni taqdim etadi.

🗂 Python ma'lumotlar fani va ma'lumotlarni tahlil qilishda ham keng qo'llaniladi, bu esa uni katta hajmdagi ma'lumotlarni qayta ishlash va mashinani o'rganish bilan bog'liq tizimlarni backend ishlab chiqish uchun foydali qiladi.

🪩 Backend Python ishlab chiquvchilari server kodini yaratish va optimallashtirish, ma'lumotlar bazasini boshqarish, so'rovlarni qayta ishlash, biznes mantig'ini amalga oshirish va ilovaning xavfsizligi va ishlashini ta'minlash bilan shug'ullanadi.

📚 Backend Python Python tilining soddaligi va ekspressivligi, keng funktsionalligi va kutubxonalar va ramkalarning boy ekotizimi tufayli ko'plab ishlab chiquvchilar uchun mashhur tanlovdir."""
    await call.message.answer(text, reply_markup=backend_inl)


@dp.callback_query_handler(text='1b')
async def misol(call: types.CallbackQuery):
    await call.message.delete()
    album = [open('static/document/mvt/orbit_resume.zip', 'rb'), open('static/document/mvt/ronaldo_resume.zip', 'rb'),
             open('static/document/mvt/louie_resume.zip', 'rb')]
    text = ["<a href='https://preview.colorlib.com/theme/orbit/'>Orbit sayt link</a>",
            "<a href='https://preview.colorlib.com/theme/ronaldo/'>Ronaldo sayt link</a>",
            "<a href='https://preview.colorlib.com/theme/louie/'>Louie sayt link</a>"]
    for i in range(len(album)):
        await call.message.answer_document(document=album[i], caption=text[i])
    await call.message.answer("Resume sayt uchun shablonlar", reply_markup=mvt_aloqar_inl)


@dp.callback_query_handler(text='2b')
async def misol(call: types.CallbackQuery):
    await call.message.delete()
    album = [open('static/document/mvt/moose_blog.zip', 'rb'), open('static/document/mvt/readit_blog.zip', 'rb'),
             open('static/document/mvt/wordify_blog.zip', 'rb')]
    text = ["<a href='https://preview.colorlib.com/theme/moose/'>Moose sayt link</a>",
            "<a href='https://preview.colorlib.com/theme/readit/'>Redit sayt link</a>",
            "<a href='https://preview.colorlib.com/theme/wordify/'>Wordify sayt link</a>"]
    for i in range(len(album)):
        await call.message.answer_document(document=album[i], caption=text[i])
    await call.message.answer("Blog sayt uchun shablonlar", reply_markup=mvt_aloqar_inl)


@dp.callback_query_handler(text='3b')
async def misol(call: types.CallbackQuery):
    await call.message.delete()
    album = [open('static/document/mvt/cozastore_ec.zip', 'rb'), open('static/document/mvt/amado_ec.zip', 'rb')]
    text = ["<a href='https://preview.colorlib.com/theme/cozastore/'>Cozastore sayt link</a>",
            "<a href='https://preview.colorlib.com/theme/amado/'>Amado sayt link</a>"]
    for i in range(len(album)):
        await call.message.answer_document(document=album[i], caption=text[i])
    await call.message.answer("eCommerce sayt uchun shablonlar", reply_markup=mvt_aloqar_inl)
