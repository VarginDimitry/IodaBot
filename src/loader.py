from aiogram import Bot
from aiogram.enums import ParseMode

from src.EnvManager import EnvManager

EnvManager.load_env()
bot = Bot(EnvManager.TOKEN(), parse_mode=ParseMode.HTML)
