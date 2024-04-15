from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.menu import menu_uchun
from loader import dp

from funksiya.funksiya import downloader_media
from loader import dp, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"""🔥 Xush kelibsiz, siz bot orqali yuklab olishingiz mumkin:

    • Instagram - istalgan formatdagi hikoyalar, postlar va IGTV!:

    🚀 Mediani yuklab olishni boshlash uchun havolani yuborin:

    👨‍💻 Admin: @Madara_zona""", reply_markup=menu_uchun)


@dp.message_handler(regexp=r'instagram.com')
async def instagram_handler(message: types.Message):
    result = await downloader_media(message.text)
    input_media = types.MediaGroup()
    if result:
        if result['images'] != []:
            for x in result['images']:
                input_media.attach_photo(x)
        if result['videos'] != []:
            for x in result['videos']:
                input_media.attach_video(x)

    await bot.send_media_group(chat_id=message.chat.id, media=input_media)
