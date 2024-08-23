from aiogram import types

from keyboards.inline.tarmoqlar_inline import aloqar_inl
from keyboards.inline.misolar_inline import foundation_inl, bot_inl, backend_inl
from keyboards.inline.backend_inline import course_inl
from loader import dp


@dp.message_handler(text='🎓 Kurs haqida ma’lumotlar (Online)')
async def bot_start(message: types.Message):
    img = open('static/image/online.jpg', 'rb')
    text = """📌 Python Foundation, Telegram Bot va Python Backend bo'yicha onlayn individual darslar

📚 Python Foundation bo'yicha darslar:
Python dasturlash tilini o'rganishni istaysizmi? Bizning individual onlayn darslarimiz orqali Python asoslarini mukammal o'zlashtirishingiz mumkin.

👨🏻‍💻 Telegram Bot yaratish bo'yicha darslar:
Telegram botlarini yaratishni o'rganmoqchimisiz? Bizning darslarimiz sizga Python yordamida kuchli va foydali Telegram botlarini yaratish bo'yicha bilim va ko'nikmalarni beradi.

🐍 Python Backend bo'yicha darslar:
Web-ilovalar va dasturiy tizimlarning orqa qismini yaratishni o'rganishni xohlaysizmi? Python backend dasturlarini ishlab chiqish bo'yicha individual darslarimiz sizga kerakli bilim va tajribani taqdim etadi."""
    await message.answer_photo(img, caption=text, reply_markup=course_inl)
    await message.delete()


@dp.callback_query_handler(text='foundation')
async def bot_found(call: types.CallbackQuery):
    await call.message.delete()
    text = """📌 Dasturlash asoslarini o'rganish bir nechta muhim sabablarga ega:

📚 Dasturlash mantig'ini tushunish: dasturlash asoslari dasturlarning mantig'i va ishlash tamoyillarini tushunishga imkon beradi. Siz kompyuterlar ma'lumotni qanday qayta ishlashini va ma'lumotlar bilan qanday munosabatda bo'lishini bilib olasiz.

🔍 Algoritmik fikrlashni rivojlantirish: dasturlash asoslarini o'rganish algoritmik fikrlash ko'nikmalarini va murakkab vazifalarni sodda va tushunarli bosqichlarga bo'lish qobiliyatini rivojlantirishga yordam beradi. Siz samarali muammolarni hal qilish algoritmlarini ishlab chiqishingiz mumkin.

👥  Jamoa bilan ishlash: dasturlash asoslarini bilish sizga boshqa ishlab chiquvchilar bilan samarali hamkorlik qilish imkonini beradi. Siz umumiy tilda tushunishingiz va muloqot qilishingiz, boshqa ishlab chiquvchilar tomonidan yaratilgan kodni osonroq ajratishingiz va tushunishingiz mumkin.

🚀 Analitik fikrlashni rivojlantirish: dasturlash asoslarini o'rganish analitik fikrlash va muammolarni muntazam ravishda hal qilish qobiliyatini rivojlantiradi. Siz muammolarni tahlil qilishni, ularning sabablarini topishni va oqilona echimlarni ishlab chiqishni o'rganasiz.

🦾 Texnologiyaning texnik tomonini tushunish: texnologiyaga boy dunyoda dasturlash asoslarini tushunish sizga texnik echimlar va texnologik mahsulotlar bilan yaxshiroq tushunish va o'zaro aloqada bo'lishga yordam beradi.

🎓 Dasturlash asoslarini o'rganish sizga nafaqat o'ziga xos dasturlash ko'nikmalarini beradi, balki tanqidiy fikrlash, ijodkorlik va muammoli fikrlashni rivojlantirishga yordam beradi. Ushbu ko'nikmalar nafaqat dasturlash sohasida, balki faoliyatning turli sohalarida ham qimmatli va foydalidir."""
    await call.message.answer(text, reply_markup=foundation_inl)


@dp.callback_query_handler(text='bot')
async def bot_found(call: types.CallbackQuery):
    await call.message.delete()
    text = """📌 <b>Telegram bot</b> Telegram messenjerida ishlaydigan avtomatlashtirilgan dasturiy ta'minot bo'lib, u foydalanuvchilarga turli vazifalarni bajarishda yordam beradi. Botlar avtomatik javob berish, ma'lumot taqdim etish, interaktiv xizmatlar ko'rsatish va boshqa ko'plab vazifalarni amalga oshiradi.

🗣 Telegram botlar foydalanuvchi so'rovlariga javob berish, ma'lumotlarni qayta ishlash, API lar bilan integratsiya qilish va boshqa ko'plab funktsiyalarni bajarish uchun ishlab chiqilgan. Ular foydalanuvchi bilan muloqot qilish uchun matn, rasmlar, videolar, tugmalar va boshqa interaktiv elementlarni ishlatishi mumkin.

🐍 Python Telegram botlarini yaratishda keng qo'llaniladigan dasturlash tillaridan biridir. Python uchun mavjud bo'lgan kutubxonalar va ramkalar Telegram botlarini yaratishni osonlashtiradi. Ushbu kutubxonalarga pyTelegramBotAPI, python-telegram-bot va telepot kiradi. Ular botlarni yaratish, xabarlarni qayta ishlash, tugmalar va menyularni sozlash kabi vazifalarni osonlashtiradi.

🗂 Telegram botlari foydalanuvchilarga turli xizmatlarni taqdim etishi mumkin, jumladan, ob-havo ma'lumotlari, yangiliklar yangilanishlari, savdo jarayonlari, o'yinlar va ko'ngilochar xizmatlar, ma'lumotlar bazasidan ma'lumotlar olish va boshqalar.

🛠 Telegram bot ishlab chiquvchilari botning logikasini yaratish, foydalanuvchi interfeysi bilan ishlash, ma'lumotlar bazasi bilan integratsiya qilish va xavfsizlikni ta'minlash kabi vazifalar bilan shug'ullanadi. Shuningdek, ular botning ishlashini va foydalanuvchi tajribasini yaxshilash uchun muntazam ravishda optimallashtirish va yangilash ishlarini olib boradilar.

💰 Telegram botlari nafaqat foydalanuvchilarga qulaylik yaratadi, balki bizneslar uchun ham katta foyda keltiradi. Ular mijozlar bilan avtomatlashtirilgan muloqot o'rnatish, mijozlarga xizmat ko'rsatishni yaxshilash va xarajatlarni kamaytirishga yordam beradi. Python ning qulayligi va kuchli kutubxonalari Telegram botlarini yaratishda uni ideal tanlov qiladi."""
    await call.message.answer(text, reply_markup=bot_inl)


@dp.callback_query_handler(text='backend')
async def bot_found(call: types.CallbackQuery):
    await call.message.delete()
    text = """📌 Backend Python  dasturlash tili veb-ilovalar va boshqa dasturiy tizimlarning orqa qismini yaratish va boshqarish uchun ishlatiladigan dasturiy ta'minotni ishlab chiqishni anglatadi.

👨🏻‍💻 Python backend-bu mijoz tomoni (frontend) so'rovlarini ko'rib chiqadigan va ma'lumotlar bazalari bilan o'zaro aloqada bo'lgan, biznes mantig'ini bajaradigan, xavfsizlik, ma'lumotlarni qayta ishlash va boshqa funktsiyalarni ta'minlaydigan dasturlarning server tomoni.

🐍 Python backend dasturlarini ishlab chiqishni osonlashtiradigan ko'plab kutubxonalar va ramkalarni taklif etadi. Backend rivojlanishi uchun ba'zi mashhur Python ramkalariga Django, Flask, Pyramid va Bottle kiradi. Ular marshrutlarni boshqarish, ma'lumotlar bazalari bilan ishlash, API ishlab chiqish va backend ishlab chiqish uchun zarur bo'lgan boshqa vazifalar uchun qulay vositalarni taqdim etadi.

🗂 Python ma'lumotlar fani va ma'lumotlarni tahlil qilishda ham keng qo'llaniladi, bu esa uni katta hajmdagi ma'lumotlarni qayta ishlash va mashinani o'rganish bilan bog'liq tizimlarni backend ishlab chiqish uchun foydali qiladi.

🪩 Backend Python ishlab chiquvchilari server kodini yaratish va optimallashtirish, ma'lumotlar bazasini boshqarish, so'rovlarni qayta ishlash, biznes mantig'ini amalga oshirish va ilovaning xavfsizligi va ishlashini ta'minlash bilan shug'ullanadi.

📚 Backend Python Python tilining soddaligi va ekspressivligi, keng funktsionalligi va kutubxonalar va ramkalarning boy ekotizimi tufayli ko'plab ishlab chiquvchilar uchun mashhur tanlovdir."""
    await call.message.answer(text, reply_markup=backend_inl)


@dp.callback_query_handler(text='noutbuk')
async def bot_start(call: types.CallbackQuery):
    await call.message.delete()
    text = """👨🏻‍💻 Dasturlash uchun talab qilinadigan minimum noutbuk, agar yangi olmoqchi bo’lsangiz:

🔸 Kami bilan Core i5 (10-avlod) yoki AMD Ryzen 5 (Core i7 bo’lsa yaxshi)
🔸 Tezkor xotira RAM kami bilan 8GB (16 bo'lsa yaxshi)\- Asosiy Xotira SSD kami bilan 256 GB

💻 Agar Apple MacBook olmoqchi bo’lsangiz va pulingiz yetarli bo’lsa:

🔹 Kami bilan M1 Protsessor
🔹 Kami bilan 8GB RAM xotira
🔹 Kami bilan 256GB doimiy SSD xotira

🖥 Agar oldingi kompyuteringiz bo’lsa uning texnik holatini quyidagilarga keltirib olishingiz maqsadga muvofiq:

🔻 RAM xotira 8GB kamida;
🔻 Agar HDD xotira bo’lsa, uni kamida 256GB SSDga almashtirish yoki HDD yoniga o’rnatish"""
    await call.message.answer(text, reply_markup=aloqar_inl)


@dp.callback_query_handler(text='backk')
async def resume(call: types.CallbackQuery):
    await call.message.delete()
    img = open('static/image/online.jpg', 'rb')
    text = """📌 Python Foundation, Telegram Bot va Python Backend bo'yicha onlayn individual darslar

📚 Python Foundation bo'yicha darslar:
Python dasturlash tilini o'rganishni istaysizmi? Bizning individual onlayn darslarimiz orqali Python asoslarini mukammal o'zlashtirishingiz mumkin.

👨🏻‍💻 Telegram Bot yaratish bo'yicha darslar:
Telegram botlarini yaratishni o'rganmoqchimisiz? Bizning darslarimiz sizga Python yordamida kuchli va foydali Telegram botlarini yaratish bo'yicha bilim va ko'nikmalarni beradi.

🐍 Python Backend bo'yicha darslar:
Web-ilovalar va dasturiy tizimlarning orqa qismini yaratishni o'rganishni xohlaysizmi? Python backend dasturlarini ishlab chiqish bo'yicha individual darslarimiz sizga kerakli bilim va tajribani taqdim etadi."""
    await call.message.answer_photo(img, caption=text, reply_markup=course_inl)
