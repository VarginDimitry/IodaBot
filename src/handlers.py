import aiohttp
from aiogram import Router, F
from aiogram.enums import ContentType
from aiogram.types import Message


router = Router(name=__name__)


@router.message(F.content_type == ContentType.TEXT)
async def echo(message: Message) -> None:

    await message.answer(message.text)
