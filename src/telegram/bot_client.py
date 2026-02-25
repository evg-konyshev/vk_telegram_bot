from retry import retry

from core.logger import get_logger
from core.settings import get_settings

from httpx import Client, HTTPError

settings = get_settings()

logger = get_logger(__name__)

class TelegramBotClient:

    def __init__(
        self,
    ) -> None:
        self._client = Client(base_url=settings.bot_url)
        logger.debug("TelegramBotClient initialized")

    @retry(HTTPError, delay=1, backoff=2)
    def send_to_telegram(self, message_text: str):
        try:
            data = {
                'chat_id': settings.TELEGRAM_CHAT_ID,
                'text': message_text
            }
            url = settings.SEND_MESSAGE_URL
            response = self._client.post(url, data=data)
            response.raise_for_status()
            return response.json()
        except HTTPError as e:
            logger.exception(f"Ошибка отправки сообщения в Telegram: {e}")
            raise