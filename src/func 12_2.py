import logging
from datetime import datetime

logger = logging.getLogger('daily_logger')
logger.setLevel(logging.DEBUG)

log_filename = datetime.now().strftime('%Y-%m-%d.log')
file_handler = logging.FileHandler(log_filename, mode='a')
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def log_messages(level: str, message: str):
    """Логирует сообщения разных уровней в ежедневные лог-файлы."""
    if level == "info":
        logger.info(message)
    elif level == "warning":
        logger.warning(message)
    elif level == "error":
        logger.error(message)
    else:
        logger.warning(f"неизвестный уровень лога: {level}. Message: {message}")


if __name__ == "__main__":
    log_messages("info", "Это информационное сообщение.")
    log_messages("warning", "Это предупреждение.")
    log_messages("error", "Это ошибка.")


logger = logging.getLogger('daily_logger_2')
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

log_filename = datetime.now().strftime('%Y-%m-%d.log')
file_handler = logging.FileHandler(log_filename)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)


def log_messages_to_console(level: str, message: str):
    """Логирует сообщения разных уровней в ежедневные лог-файлы и консоль"""
    if level == "info":
        logger.info(message)
    elif level == "warning":
        logger.warning(message)
    elif level == "error":
        logger.error(message)
    else:
        logger.warning(f"неизвестный уровень лога: {level}. Message: {message}")


if __name__ == "__main__":
    log_messages("info", "Это информационное сообщение.")
    log_messages("warning", "Это предупреждение.")
    log_messages("error", "Это ошибка.")
