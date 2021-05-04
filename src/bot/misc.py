import aiogram
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from src.core.settings import Settings

bot = aiogram.Bot(Settings.TOKEN)
bot.parse_mode = "HTML"
dp = aiogram.dispatcher.Dispatcher(bot, storage=MemoryStorage())
