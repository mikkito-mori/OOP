"""Миксин сквозного логирования действий объектов."""

import logging


class LoggingMixin:
    """Добавляет объекту методы логирования с меткой имени класса."""
    __slots__ = ()

    def log(self, message: str) -> None:
        """Информационное сообщение (INFO)."""
        logger = logging.getLogger(self.__class__.__name__)
        if not logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                "[%(name)s] %(levelname)s: %(message)s"
            )
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            logger.setLevel(logging.INFO)
        logger.info(message)

    def log_warning(self, message: str) -> None:
        """Предупреждение (WARNING)."""
        logging.getLogger(self.__class__.__name__).warning(message)

    def log_error(self, message: str) -> None:
        """Ошибка (ERROR)."""
        logging.getLogger(self.__class__.__name__).error(message)
