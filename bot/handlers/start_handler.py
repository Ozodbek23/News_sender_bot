from aiogram import types
from aiogram.utils import executor
from aiogram.dispatcher.storage import FSMContext
from bot.handlers import *
from bot.dispacher import dp
from bot.buttons.reply import news_site
import logging



@dp.message_handler(commands='news')
async def start_func(msg : types.Message , state : FSMContext):
    await msg.answer("Choose from which site you want to recieve the news 👇" , reply_markup=news_site())
    await state.set_state("news_site_set")


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)