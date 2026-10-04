"""Тесты для dataclass-конфигураций."""

import pytest
from core.config import GameConfig, PlayerConfig, BoardConfig


class TestConfig:
    def test_game_config_frozen(self):
        """Попытка изменить поле в GameConfig вызывает ошибку (frozen=True)."""
        cfg = GameConfig()
        with pytest.raises(Exception):
            cfg.grid_size = 5

    def test_game_config_defaults(self):
        """Значения по умолчанию корректны."""
        cfg = GameConfig()
        assert cfg.grid_size == 3
        assert cfg.win_length == 3
        assert cfg.max_moves == 9

    def test_game_config_equality(self):
        """Два одинаковых конфига равны."""
        a = GameConfig()
        b = GameConfig()
        assert a == b

    def test_board_config_independent_lists(self):
        """default_factory создаёт независимые списки истории ходов."""
        b1 = BoardConfig()
        b2 = BoardConfig()
        b1.history.append((0, 0, "X"))
        assert b1.history == [(0, 0, "X")]
        assert b2.history == []
