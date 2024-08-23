from aiogram import types

from keyboards.inline.tarmoqlar_inline import bot_aloqar_inl
from keyboards.inline.misolar_inline import bot_inl
from loader import dp


@dp.callback_query_handler(text='boochiqdars')
async def bot_found(call: types.CallbackQuery):
    await call.message.delete()
    text = '📹 Telegram bot ochiq dars video tayorlanmoqda tez orada botga joylanadi...'
    await call.message.answer(text, reply_markup=bot_aloqar_inl)


@dp.callback_query_handler(text='bokursdavomida')
async def bot_found(call: types.CallbackQuery):
    await call.message.delete()
    img = open('static/image/bot.jpg', 'rb')
    text = """🤖 Kursing davomiyligi 2 oy bo’lib, haftada 3 kun 1, 1.5 soat dan bo’lib o’tadi. Kurs davomida siz:

— Telegram Bot ning boshlang'ich tushunchalari; 
— Bir nechta soda botlar yaratish;
— Default Keyboard va Inline keyboard bilan ishlash;
— Qo'shimcha funksiyalar bilan ishlash(Hujjatlar va media);
— Bot uchun shablon bilan tanishish;
— Handlers (Filterlar);
— Guruxlar bilan ishlovchi botlar;
— Kanallar bilan ishlovchi botlar;
— Ma`lumotlar ombori. SQLITE;
— BOT orqali to'lov;
— Botni serverga yuklash;
— GitHub bilan ishlashni o'rganish;


💸 Kurslarning narxiga keladigan bo'lsak

🔰 Oldindan oyiga to’lov:
   👤 Individual 1 200 000  so'm.
   👥 Gurux bilan  800 000 so'm"""
    await call.message.answer_photo(photo=img, caption=text, reply_markup=bot_aloqar_inl)


@dp.callback_query_handler(text='botshablon')
async def bot_found(call: types.CallbackQuery):
    await call.message.delete()
    img = open('static/document/shablon.zip', 'rb')
    text = '<b>Telegram bot shabloni</b>'
    await call.message.answer_document(document=img, caption=text, reply_markup=bot_aloqar_inl)


@dp.callback_query_handler(text='botback')
async def bot_found(call: types.CallbackQuery):
    await call.message.delete()
    text = """📌 <b>Telegram bot</b> Telegram messenjerida ishlaydigan avtomatlashtirilgan dasturiy ta'minot bo'lib, u foydalanuvchilarga turli vazifalarni bajarishda yordam beradi. Botlar avtomatik javob berish, ma'lumot taqdim etish, interaktiv xizmatlar ko'rsatish va boshqa ko'plab vazifalarni amalga oshiradi.

🗣 Telegram botlar foydalanuvchi so'rovlariga javob berish, ma'lumotlarni qayta ishlash, API lar bilan integratsiya qilish va boshqa ko'plab funktsiyalarni bajarish uchun ishlab chiqilgan. Ular foydalanuvchi bilan muloqot qilish uchun matn, rasmlar, videolar, tugmalar va boshqa interaktiv elementlarni ishlatishi mumkin.

🐍 Python Telegram botlarini yaratishda keng qo'llaniladigan dasturlash tillaridan biridir. Python uchun mavjud bo'lgan kutubxonalar va ramkalar Telegram botlarini yaratishni osonlashtiradi. Ushbu kutubxonalarga pyTelegramBotAPI, python-telegram-bot va telepot kiradi. Ular botlarni yaratish, xabarlarni qayta ishlash, tugmalar va menyularni sozlash kabi vazifalarni osonlashtiradi.

🗂 Telegram botlari foydalanuvchilarga turli xizmatlarni taqdim etishi mumkin, jumladan, ob-havo ma'lumotlari, yangiliklar yangilanishlari, savdo jarayonlari, o'yinlar va ko'ngilochar xizmatlar, ma'lumotlar bazasidan ma'lumotlar olish va boshqalar.

🛠 Telegram bot ishlab chiquvchilari botning logikasini yaratish, foydalanuvchi interfeysi bilan ishlash, ma'lumotlar bazasi bilan integratsiya qilish va xavfsizlikni ta'minlash kabi vazifalar bilan shug'ullanadi. Shuningdek, ular botning ishlashini va foydalanuvchi tajribasini yaxshilash uchun muntazam ravishda optimallashtirish va yangilash ishlarini olib boradilar.

💰 Telegram botlari nafaqat foydalanuvchilarga qulaylik yaratadi, balki bizneslar uchun ham katta foyda keltiradi. Ular mijozlar bilan avtomatlashtirilgan muloqot o'rnatish, mijozlarga xizmat ko'rsatishni yaxshilash va xarajatlarni kamaytirishga yordam beradi. Python ning qulayligi va kuchli kutubxonalari Telegram botlarini yaratishda uni ideal tanlov qiladi."""
    await call.message.answer(text, reply_markup=bot_inl)