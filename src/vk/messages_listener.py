from typing import Generator

from urllib3.exceptions import ReadTimeoutError
from vk_api.longpoll import Event
from requests import ReadTimeout
from retry import retry

from core.logger import get_logger
from core.settings import get_settings
from src.vk.connection import get_long_pool, get_connection

settings = get_settings()
logger = get_logger(__name__)


class VKGroupEventsListener:
    def __init__(self):
        self._connection = get_connection()
        self._longpool = get_long_pool()
        logger.debug("VKGroupEventsListener initialized")

    def get_messages(self):
        ...

    @retry((ReadTimeout, ReadTimeoutError), delay=1, backoff=2)
    def listen(self) -> Generator[Event, None, None]:
        for event in self._longpool.listen():
            yield event