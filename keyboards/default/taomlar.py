from aiogram .types import ReplyKeyboardMarkup, KeyboardButton

tasdiqlash_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Tasdiqlash✅"),
            KeyboardButton(text="Bekor qilish❌")

        ]
    ],
    resize_keyboard=True
)