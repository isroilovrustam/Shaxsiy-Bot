from keyboards.inline.register_inl import reg_course, reg_course_types
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.inline.rustam_inl import ha_yoq_register, ha_yoq_tasdiq
from loader import dp, bot
from states.person import CourseState
from keyboards.default.start_keyboard import contact_btn, start_btn

GROUP_ID = -4535946756


@dp.message_handler(text="📝 Kursga ro'yxatdan o'tish")
async def enter_test(message: types.Message):
    await message.answer(f"Salom {message.from_user.full_name} Kurslardan biriga ro'yxatdan o'tishni xohlaysizmi ⁉️",
                         reply_markup=ha_yoq_register)


@dp.callback_query_handler(text='yoqr')
async def hsa(call: types.CallbackQuery):
    await call.message.answer("Ro'yxatdan o'tish bekor qilindi !!")
    await call.message.delete()


@dp.callback_query_handler(text='har')
async def hsa(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("‼️ Hozir sizga bir nechta savolar beriladi.")
    await call.message.answer("Ism, familiyangizni kiriting?", reply_markup=types.ReplyKeyboardRemove())
    await CourseState.full_name.set()


@dp.message_handler(state=CourseState.full_name)
async def answer_fullname(message: types.Message, state: FSMContext):
    fullname = message.text

    await state.update_data(
        {"username": message.from_user.username}
    )

    await state.update_data(
        {"name": fullname}
    )

    await message.answer("Telefon raqamingizni kiriting?", reply_markup=contact_btn)

    await CourseState.phone_number.set()


@dp.message_handler(content_types=['contact', 'text'], state=CourseState.phone_number)
async def answer_email(message: types.Message, state: FSMContext):
    if message.contact:
        phone = message.contact.phone_number
    # Oddiy xabar orqali yuborilgan raqam
    else:
        phone = message.text

    await state.update_data(
        {"phone": phone},

    )

    await message.answer("Qanday kursga o'qimoqchisiz?",
                         reply_markup=reg_course)

    await CourseState.course_title.set()


@dp.callback_query_handler(text=["regfoun", "regbot", "regback"], state=CourseState.course_title)
async def answer_email(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    course_name = call.data
    if course_name == "regfoun":
        course = "Foundation"
    elif course_name == "regbot":
        course = "Telegram Bot"
    elif course_name == "regback":
        course = "Python Backend"
    await state.update_data(
        {"course": course}
    )

    await call.message.answer("Kurs turini tanlang?", reply_markup=reg_course_types)

    await CourseState.course_type.set()


@dp.callback_query_handler(text=["regindi", "reggur"], state=CourseState.course_type)
async def answer_phone(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    type_course = call.data
    if type_course == "regindi":
        type = "Individual"
    elif type_course == "reggur":
        type = "Gurux"

    await state.update_data(
        {"type": type}
    )

    # Ma`lumotlarni qayta o'qiymiz
    data = await state.get_data()
    name = data.get("name")
    phone = data.get("phone")
    username = data.get("username")
    course = data.get("course")
    type = data.get("type")

    msg = f"Ma'lumotlar:\n\n"
    msg += f"👨‍💼 Ismingiz - {name}\n"
    msg += f"📞 Telefon: - {phone}\n"
    msg += f"🇺🇿 Telegram: - @{username}\n"
    msg += f"👨🏻‍💻 Kurs - {course}\n"
    msg += f"🎓 Kurs turi - {type}\n\n"
    msg += "‼️ Barcha ma'lumotlar to'g'rimi ‼️"

    await call.message.answer(msg, reply_markup=ha_yoq_tasdiq)


@dp.callback_query_handler(state=CourseState, text='hat')
async def submit_data(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    name = data.get("name")
    phone = data.get("phone")
    username = data.get("username")
    course = data.get("course")
    type = data.get("type")

    msg = f"Yangi ro'yxatdan o'tish:\n\n"
    msg += f"👨‍💼 Ismingiz - {name}\n"
    msg += f"📞 Telefon: - {phone}\n"
    msg += f"🇺🇿 Telegram: - @{username}\n"
    msg += f"👨🏻‍💻 Kurs - {course}\n"
    msg += f"🎓 Kurs turi - {type}\n"

    # Ma'lumotlarni guruhga yuborish
    await bot.send_message(GROUP_ID, msg)

    await call.message.delete()
    await call.message.answer("✅ Ma'lumotlaringiz yuborildi!!!", reply_markup=start_btn)
    await state.finish()


@dp.callback_query_handler(state=CourseState, text='yoqt')
async def hsa(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer("🚫 Ma'lumotingiz yuborilmadi!!!", reply_markup=start_btn)
    await call.message.delete()
    await state.finish()




