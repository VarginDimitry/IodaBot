from aiogram import Dispatcher

from handlers.alerts import alerts_router


def get_dispatcher(storage):
    dispatcher = Dispatcher(storage=storage)
    dispatcher.include_router(alerts_router)
    return dispatcher
