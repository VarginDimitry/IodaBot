import asyncio
import logging
import sys

from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.types import BotCommand

from config import settings
from fixtures import on_start_up
from handlers import get_dispatcher
import texts.alerts


async def main():
    dp = get_dispatcher(storage=RedisStorage.from_url(settings.REDIS_URL))

    bot = Bot(settings.TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await bot.set_my_commands([
        BotCommand(command="start", description=texts.alerts.START_COMMAND),
        BotCommand(command="help", description=texts.alerts.HELP_COMMAND),
        BotCommand(command="alerts", description=texts.alerts.ALERTS_COMMAND),
        BotCommand(command="cancel", description=texts.alerts.CANCEL_COMMAND),
    ])
    await on_start_up(dp)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
    asyncio.run(main())
