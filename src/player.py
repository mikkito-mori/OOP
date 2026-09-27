"""Модуль игрока."""


class Player:
    """Сущность игрока с именем и игровым символом."""

    def __init__(self, name: str, symbol: str) -> None:
        self._name = name
        self._symbol = symbol

    @property
    def name(self) -> str:
        return self._name

    @property
    def symbol(self) -> str:
        return self._symbol
