import logging
from bot.handlers import *
from aiogram.utils import executor

from bot.dispacher import dp



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)