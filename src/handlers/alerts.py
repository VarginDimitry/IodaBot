from datetime import datetime

from aiogram import Router, F
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message

from keys import Keys
from utils.ioda_manager import IODAManager
from utils.parsers import datetime_msg_parser

alerts_router = Router(name=__name__)


class AlertsForm(StatesGroup):
    from_time = State()
    until_time = State()
    country_code = State()


@alerts_router.message(Command("start"))
async def alerts(message: Message, state: FSMContext) -> None:
    await message.answer("Hello! Send /alerts to get alerts")


@alerts_router.message(Command("alerts"))
async def alerts(message: Message, state: FSMContext) -> None:
    await state.set_state(AlertsForm.from_time)
    await message.answer("Send from-time like iso or timestamp")


@alerts_router.message(F.text, AlertsForm.from_time)
async def get_from_time(message: Message, state: FSMContext) -> None:
    from_dt = datetime_msg_parser(message.text)
    if from_dt is None:
        await message.answer("Wrong datetime format")
        return

    await state.update_data({Keys.FROM: int(from_dt.timestamp())})
    await state.set_state(AlertsForm.until_time)
    await message.answer("Send until-time like iso or timestamp")


@alerts_router.message(F.text, AlertsForm.until_time)
async def get_until_time(message: Message, state: FSMContext) -> None:
    until_dt = datetime_msg_parser(message.text)
    if until_dt is None:
        await message.answer("Wrong datetime format")
        return

    await state.update_data({Keys.UNTIL: int(until_dt.timestamp())})
    await state.set_state(AlertsForm.country_code)
    await message.answer("Send country code")


@alerts_router.message(F.text, AlertsForm.country_code)
async def finish_alerts(message: Message, state: FSMContext) -> None:
    country_code = message.text.strip()
    if country_code not in await IODAManager.get_country_codes():
        await message.answer("Wrong country code")
        return

    await state.update_data({Keys.COUNTRY_CODE: country_code})

    resp = await IODAManager.get_alerts(**(await state.get_data()))

    await state.clear()

    sources = [source for source in resp.data if source.level != "normal"]

    if not sources:
        await message.answer("ALL GOOD!")
        return

    for source in sources:
        await message.answer(
            f"datasource: {source.datasource}\n"
            f"level: {source.level}\n"
            f"time: {source.time.strftime('%Y.%m.%m %H:%M:%S')}"
        )
