import asyncio

from aiogram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from src.core.tables import get_new_quizzes, AfterQuiz, update_current_quiz_sent

from src.core.settings import Settings
from src.bot.keyboards import keyboard_after_quiz
from src.bot.utils import text_formater, texts


async def cron_starter(bot, inverval):
    print('start cron', 'inverval:', inverval)
    scheduler = AsyncIOScheduler()
    scheduler.add_job(send_from_db_message, 'interval', seconds=inverval, args=(bot,), replace_existing=True)
    scheduler.start()


async def send_from_db_message(bot: Bot):
    statuses = texts.statuses_to_btn

    quizs = get_new_quizzes()

    for quiz in quizs:
        quiz: AfterQuiz
        keyboard = await keyboard_after_quiz(statuses, quiz.id, index_to_pass=0)
        if quiz.type_number == 1:
            await bot.send_message(Settings.CHANNEL, text_formater.get_text_after_quiz(quiz), reply_markup=keyboard)
        else:
            await bot.send_message(Settings.CHANNEL, text_formater.get_text_back_call(quiz), reply_markup=keyboard)

        update_current_quiz_sent(quiz)
        await asyncio.sleep(0.5)
