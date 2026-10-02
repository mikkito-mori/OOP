"""Абстрактный базовый класс для всех игровых сущностей."""

from abc import ABC, abstractmethod


class GameObject(ABC):
    """Базовый класс для всего, что существует в игровом мире."""

    _next_id: int = 0

    def __init__(self, name: str):
        self._id = GameObject._next_id
        GameObject._next_id += 1
        self._name = name
        self._active = True

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def active(self) -> bool:
        return self._active

    def deactivate(self) -> None:
        """Пометить объект как неактивный."""
        self._active = False

    @abstractmethod
    def update(self, dt: float) -> None:
        """Обновить состояние объекта за время dt."""
        ...

    @abstractmethod
    def draw(self) -> str:
        """Вернуть строковое представление для отрисовки."""
        ...

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id={self._id}, name={self._name!r})"
