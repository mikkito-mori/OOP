"""Конфигурации игры, доски и игроков."""

from dataclasses import dataclass, field


@dataclass(frozen=True)
class GameConfig:
    """Общие настройки партии крестиков-ноликов."""
    title: str = "Крестики-нолики"
    grid_size: int = 3
    win_length: int = 3
    max_moves: int = 9


@dataclass(frozen=True)
class PlayerConfig:
    """Параметры игрока."""
    name: str = "Игрок"
    symbol: str = "X"


@dataclass
class BoardConfig:
    """Конфигурация доски."""
    empty_cell: str = " "
    history: list = field(default_factory=list)
