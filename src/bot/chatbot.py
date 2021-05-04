import asyncio

import aiogram
from aiogram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from src.bot import handlers
from src.bot.misc import dp, bot
from src.bot.services.cron_services import cron_starter


async def on_startup(*args, **kwargs):
    handlers.setup(dp)
    await cron_setup(bot)
    print("Bot started")


async def cron_setup(bot: Bot):
    asyncio.create_task(cron_starter(bot, 10))


def bot_start():
    print('bot running')

    aiogram.executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

# if __name__ == '__main__':
#     bot_start()
