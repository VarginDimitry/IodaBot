import os

import dotenv


class EnvManager:

    @classmethod
    def load_env(cls) -> None:
        dotenv.load_dotenv()

    @classmethod
    def TOKEN(cls) -> str:
        return os.getenv("TOKEN")
