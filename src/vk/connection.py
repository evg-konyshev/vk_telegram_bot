from vk_api.vk_api import VkApi
from vk_api.longpoll import VkLongPoll

from core.settings import get_settings

settings = get_settings()


def get_connection() -> VkApi:
    return VkApi(token=settings.VK_GROUP_TOKEN)


def get_long_pool(session: VkApi | None = None) -> VkLongPoll:
    if session is None:
        session = get_connection()
    return VkLongPoll(session)