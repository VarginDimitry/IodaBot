import asyncio
import logging
import sys

from aiogram import Dispatcher

from src.loader import bot
from src.handlers import router


async def main():
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
    asyncio.run(main())
