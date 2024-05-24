import logging
from pathlib import Path

from pydantic import Extra
from pydantic_settings import BaseSettings

log = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent


class Settings(BaseSettings, extra=Extra.ignore):
    TZ: str
    TOKEN: str
    REDIS_URL: str = "redis://localhost:6379"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
