from aiogram.types import ReplyKeyboardMarkup

qalampir_news='Qalampir.uz'
daryo_news = "Daryo.uz"

def news_site():
    design = [
        [qalampir_news , daryo_news]
    ]
    return ReplyKeyboardMarkup(keyboard=design , resize_keyboard=True)
