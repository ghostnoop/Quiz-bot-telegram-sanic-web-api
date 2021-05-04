# from .callback_handlers import *
from aiogram import Dispatcher

from src.bot.handlers.callback_handlers import quiz_callback


def setup(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_callback, lambda c: len(c.data.split('_')) == 2)
