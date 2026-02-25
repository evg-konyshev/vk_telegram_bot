from functools import lru_cache
from typing import Literal

from pydantic import HttpUrl
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """Класс с настройками."""

    VK_GROUP_TOKEN: str
    TELEGRAM_BOT_TOKEN: str
    TELEGRAM_CHAT_ID: str

    LOG_LEVEL: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = 'INFO'

    TG_URL: HttpUrl = 'https://api.telegram.org'

    SEND_MESSAGE_URL: str = 'sendMessage'


    @property
    def bot_url(self) -> str:
        return f'{self.TG_URL}bot{self.TELEGRAM_BOT_TOKEN}'

@lru_cache
def get_settings():
    return Settings()
