import asyncio
import logging
import sys
from datetime import datetime

from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import RedisStorage

from config import settings
from fixtures import on_start_up
from handlers import get_dispatcher


async def main():
    dp = get_dispatcher(storage=RedisStorage.from_url(settings.REDIS_URL))

    bot = Bot(settings.TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await on_start_up(dp)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
    asyncio.run(main())
