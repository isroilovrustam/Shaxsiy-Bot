from aiogram import types

from loader import dp
from keyboards.inline.rustam_inl import inline_mode_btn


@dp.inline_handler()
async def inline_query_handler(query: types.InlineQuery):
    results = [
        types.InlineQueryResultDocument(
            id="pdf",
            title="Isroilov Rustam. Resume",
            document_url="https://raw.githubusercontent.com/isroilovrustam/resume/main/resume.pdf",
            mime_type="application/pdf",
            description="👨‍💻 Isroilov Rustamjonning rezyumesi bilan tanishing va batafsil ma'lumot oling.\n\n📩 Har qanday savol va takliflar uchun bog'laning!",
            thumb_url="https://raw.githubusercontent.com/isroilovrustam/resume/main/resume.pdf",
            reply_markup=inline_mode_btn
        ),
        types.InlineQueryResultArticle(
            id="git",
            title="Isroilov Rustam. GitHub",
            input_message_content=types.InputTextMessageContent(
                message_text="<b>🔗 GitHub uchun link:</b>\n\nhttps://github.com/isroilovrustam",
            ),
            url="https://github.com/isroilovrustam",
            thumb_url="https://avatars.githubusercontent.com/u/105547303?v=4",
            description="🔗 GitHub orqali qilgan proyektlarimni ko'rishingiz mumkin!!!",
            reply_markup=inline_mode_btn

        ),
        types.InlineQueryResultArticle(
            id="bot",
            title="Isroilov Rustam. Telegram Bot",
            input_message_content=types.InputTextMessageContent(
                message_text="<b>🤖 Telegram Bot:</b>\n\nBotdan foydalanib Foundation, Telegram Bot, Python Backend haqida ma'lumotlar olishingiz mumkin.\n\nhttps://t.me/abruisbot",
            ),
            url="https://t.me/abruisbot",
            thumb_url="https://raw.githubusercontent.com/isroilovrustam/resume/main/bot.png",
            description="🤖 Abruis shaxsiy telegram bot",
            reply_markup=inline_mode_btn
        ),
    ]

    await query.answer(results=results)
