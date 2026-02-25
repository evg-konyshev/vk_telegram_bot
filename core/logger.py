import logging

from core.settings import get_settings

settings = get_settings()

def get_logger(
        name: str,
        log_level: int = settings.LOG_LEVEL,
        log_format: str | None = None,
        date_format: str | None = None,
        file_handler: str | None = None
) -> logging.Logger:
    """
    Создает и настраивает логгер с заданными параметрами.

    :param name: Имя логгера
    :param log_level: Уровень логирования (по умолчанию INFO)
    :param log_format: Формат сообщений лога
    :param date_format: Формат даты в сообщениях лога
    :param file_handler: Путь к файлу для записи логов (если None - логи выводятся в консоль)
    :return: Настроенный логгер
    """
    if log_format is None:
        log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    if date_format is None:
        date_format = "%Y-%m-%d %H:%M:%S"

    # Создаем логгер
    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    # Удаляем все существующие обработчики (чтобы избежать дублирования)
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)

    # Создаем форматтер
    formatter = logging.Formatter(log_format, datefmt=date_format)

    # Создаем обработчик (консольный или файловый)
    if file_handler:
        handler = logging.FileHandler(file_handler)
    else:
        handler = logging.StreamHandler()

    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger