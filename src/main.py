from vk_api.longpoll import VkEventType

from src.vk.messages_listener import VKGroupEventsListener
from telegram.bot_client import TelegramBotClient
from core.logger import get_logger
from core.settings import get_settings

logger = get_logger(__name__)
settings = get_settings()

telegram_client = TelegramBotClient()

def listen_messages():
    chat_events_listener = VKGroupEventsListener()

    logger.info("Бот запущен. Ожидание сообщений...")
    telegram_client.send_to_telegram(
        f'Бот запущен. Ожидание сообщений'
    )
    for message in chat_events_listener.listen():
        if message.type == VkEventType.MESSAGE_NEW:
            logger.info(f'Получено новое сообщение text={message.text}, user_id={message.user_id}')
            telegram_client.send_to_telegram(
                f'[vk.com/id{message.user_id}] {message.text}'
            )


if __name__ == "__main__":
    while True:
        try:
            listen_messages()
        except Exception as e:
            logger.exception('Непредвиденная ошибка при работе')
        finally:
            telegram_client = TelegramBotClient()
            telegram_client.send_to_telegram(
                'Бот перезапущен'
            )


