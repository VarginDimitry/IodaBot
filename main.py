import asyncio
import logging
import sys

from aiogram import Dispatcher, Bot
from aiogram.enums import ParseMode

from src.utils import EnvManager
from src.handlers import router


async def main():
    dp = Dispatcher()
    dp.include_router(router)

    bot = Bot(EnvManager.TOKEN(), parse_mode=ParseMode.HTML)

    await dp.start_polling(bot)


if __name__ == '__main__':
    EnvManager.load_env()
    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
    asyncio.run(main())
