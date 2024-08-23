from aiogram import types

from keyboards.inline.tarmoqlar_inline import fonda_aloqar_inl
from keyboards.inline.misolar_inline import misolar_inl, ortga_btn, foundation_inl
from loader import dp


@dp.callback_query_handler(text="fokursdavomida")
async def bot_found(call: types.CallbackQuery):
    await call.message.delete()
    img = open('static/image/basic.png', 'rb')
    text = """💻  Kursing davomiyligi 3 oy bo’lib, haftada 3 kun 1, 1.5 soat dan bo’lib o’tadi. Kurs davomida siz:

— Python dasturlash tilining boshlang'ich tushunchalari; 
— Python da ma’lumot turlari, o’zgaruvchilar bilan ishlash;
— Axborot texnologiyalari. Kompyuterning texnik va dasturiy ta’minoti;
— Algoritm tushunchasi va turlari;
— Tartiblash algoritmlar;
— Ma'lumotlar strukturasini;
— Funksiya, satr va massivlar bilan ishlashni
— Obyektga yo'naltirilgan dasturlashni(OOP) o'rganasiz. 
— LeetCode  


💸 Kurslarning narxiga keladigan bo'lsak

🔰 Oldindan oyiga to’lov:
   👤 Individual 1 000 000  so'm.
   👥 Gurux bilan 500 000 so'm"""
    await call.message.answer_photo(photo=img, caption=text, reply_markup=fonda_aloqar_inl)


@dp.callback_query_handler(text='foundationochiq')
async def bot_found(call: types.CallbackQuery):
    await call.message.delete()
    text = '🎥 Foundation ochiq dars video tayorlanmoqda tez orada botga joylanadi...'
    await call.message.answer(text, reply_markup=fonda_aloqar_inl)


@dp.callback_query_handler(text='pythonornat')
async def bot_found(call: types.CallbackQuery):
    await call.message.delete()
    text = '📥 Pythonni o\'rnatish haqida video tayorlanmoqda tez orada botga joylanadi...'
    await call.message.answer(text, reply_markup=fonda_aloqar_inl)


@dp.callback_query_handler(text='misollar')
async def bot_found(call: types.CallbackQuery):
    await call.message.delete()
    img = open('static/image/algorithm.jpg', 'rb')
    text = """📝 <b>Foundation misolar to’plami</b>
    
1 - Print funksiyasiga doir misolar
2 - O'zgaruvchilar, Data Types, Input()
3 - Shart operatorlar
4 - While sikl operatori
5 - For sikl operatori
6 - Ro’yxatlar (List)
7 - Tuple, Set
8 - Dictionary misolar
9 - Funksiya (def)
10 - Rekursiv funksiya va *args, **kwargs
11 - 2D arrays
12 - LeetCode"""
    await call.message.answer_photo(img, caption=text, reply_markup=misolar_inl)


@dp.callback_query_handler(text='qaytish')
async def bot_found(call: types.CallbackQuery):
    await call.message.delete()
    img = open('static/image/algorithm.jpg', 'rb')
    text = """📝 <b>Foundation misolar to’plami</b>
    
1 - Print funksiyasiga doir misolar
2 - O'zgaruvchilar, Data Types, Input()
3 - Shart operatorlar
4 - While sikl operatori
5 - For sikl operatori
6 - Ro’yxatlar (List)
7 - Tuple, Set
8 - Dictionary misolar
9 - Funksiya (def)
10 - Rekursiv funksiya va *args, **kwargs
11 - 2D arrays
12 - LeetCode"""
    await call.message.answer_photo(photo=img, caption=text, reply_markup=misolar_inl)


@dp.callback_query_handler(text='foundationback')
async def foundationback(call: types.CallbackQuery):
    await call.message.delete()
    text = """📌 Dasturlash asoslarini o'rganish bir nechta muhim sabablarga ega:

    📚 Dasturlash mantig'ini tushunish: dasturlash asoslari dasturlarning mantig'i va ishlash tamoyillarini tushunishga imkon beradi. Siz kompyuterlar ma'lumotni qanday qayta ishlashini va ma'lumotlar bilan qanday munosabatda bo'lishini bilib olasiz.

    🔍 Algoritmik fikrlashni rivojlantirish: dasturlash asoslarini o'rganish algoritmik fikrlash ko'nikmalarini va murakkab vazifalarni sodda va tushunarli bosqichlarga bo'lish qobiliyatini rivojlantirishga yordam beradi. Siz samarali muammolarni hal qilish algoritmlarini ishlab chiqishingiz mumkin.

    👥  Jamoa bilan ishlash: dasturlash asoslarini bilish sizga boshqa ishlab chiquvchilar bilan samarali hamkorlik qilish imkonini beradi. Siz umumiy tilda tushunishingiz va muloqot qilishingiz, boshqa ishlab chiquvchilar tomonidan yaratilgan kodni osonroq ajratishingiz va tushunishingiz mumkin.

    🚀 Analitik fikrlashni rivojlantirish: dasturlash asoslarini o'rganish analitik fikrlash va muammolarni muntazam ravishda hal qilish qobiliyatini rivojlantiradi. Siz muammolarni tahlil qilishni, ularning sabablarini topishni va oqilona echimlarni ishlab chiqishni o'rganasiz.

    🦾 Texnologiyaning texnik tomonini tushunish: texnologiyaga boy dunyoda dasturlash asoslarini tushunish sizga texnik echimlar va texnologik mahsulotlar bilan yaxshiroq tushunish va o'zaro aloqada bo'lishga yordam beradi.

    🎓 Dasturlash asoslarini o'rganish sizga nafaqat o'ziga xos dasturlash ko'nikmalarini beradi, balki tanqidiy fikrlash, ijodkorlik va muammoli fikrlashni rivojlantirishga yordam beradi. Ushbu ko'nikmalar nafaqat dasturlash sohasida, balki faoliyatning turli sohalarida ham qimmatli va foydalidir."""
    await call.message.answer(text, reply_markup=foundation_inl)


@dp.callback_query_handler(text='1')
async def misol(call: types.CallbackQuery):
    img = open('static/document/misolar/print.pdf', 'rb')
    await call.message.delete()
    await call.message.answer_document(document=img, caption="✅ Print funksiyasiga doir misolar",
                                       reply_markup=ortga_btn)


@dp.callback_query_handler(text='2')
async def misol(call: types.CallbackQuery):
    img = open('static/document/misolar/data_types.pdf', 'rb')
    await call.message.delete()
    await call.message.answer_document(document=img, caption="✅ O'zgaruvchilar, Data Types, Input()",
                                       reply_markup=ortga_btn)


@dp.callback_query_handler(text='3')
async def misol(call: types.CallbackQuery):
    img = open('static/document/misolar/shart_operatorlar.pdf', 'rb')
    await call.message.delete()
    await call.message.answer_document(document=img, caption="✅ Shart operatorlar",
                                       reply_markup=ortga_btn)


@dp.callback_query_handler(text='4')
async def misol(call: types.CallbackQuery):
    img = open('static/document/misolar/while_for_1.pdf', 'rb')
    await call.message.delete()
    await call.message.answer_document(document=img, caption="✅ While sikl operatori",
                                       reply_markup=ortga_btn)


@dp.callback_query_handler(text='5')
async def misol(call: types.CallbackQuery):
    img = open('static/document/misolar/while_for_2.pdf', 'rb')
    await call.message.delete()
    await call.message.answer_document(document=img, caption="✅ For sikl operatori",
                                       reply_markup=ortga_btn)


@dp.callback_query_handler(text='6')
async def misol(call: types.CallbackQuery):
    img = open('static/document/misolar/listlar.pdf', 'rb')
    await call.message.delete()
    await call.message.answer_document(document=img, caption="✅ Ro’yxatlar (List)",
                                       reply_markup=ortga_btn)


@dp.callback_query_handler(text='7')
async def misol(call: types.CallbackQuery):
    img = open('static/document/misolar/setlar.pdf', 'rb')
    await call.message.delete()
    await call.message.answer_document(document=img, caption="✅ Tuple, Set",
                                       reply_markup=ortga_btn)


@dp.callback_query_handler(text='8')
async def misol(call: types.CallbackQuery):
    img = open('static/document/misolar/dictionary.pdf', 'rb')
    await call.message.delete()
    await call.message.answer_document(document=img, caption="✅ Dictionary misolar",
                                       reply_markup=ortga_btn)


@dp.callback_query_handler(text='9')
async def misol(call: types.CallbackQuery):
    img = open('static/document/misolar/funksiya.pdf', 'rb')
    await call.message.delete()
    await call.message.answer_document(document=img, caption="✅ Funksiya (def)",
                                       reply_markup=ortga_btn)


@dp.callback_query_handler(text='10')
async def misol(call: types.CallbackQuery):
    img = open('static/document/misolar/rekursiya.pdf', 'rb')
    await call.message.delete()
    await call.message.answer_document(document=img, caption="✅ Rekursiv funksiya va *args, **kwargs",
                                       reply_markup=ortga_btn)


@dp.callback_query_handler(text='11')
async def misol(call: types.CallbackQuery):
    img = open('static/document/misolar/2D_arrays.pdf', 'rb')
    await call.message.delete()
    await call.message.answer_document(document=img, caption="✅ 2D arrays",
                                       reply_markup=ortga_btn)
