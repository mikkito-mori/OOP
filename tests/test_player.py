"""Тесты класса Player и изоляции UI."""
from unittest.mock import patch
from src.player import Player
from src.ui import UI


class TestPlayerAndUI:
    """Проверяем сущность Player и валидацию координат в UI."""

    def test_player_properties(self):
        """Проверка корректной инициализации имени и символа игрока."""
        player = Player("Алиса", "X")
        assert player.name == "Алиса"
        assert player.symbol == "X"

    def test_ui_get_move_valid(self):
        """Проверка преобразования ввода в индексы матрицы 0-2."""
        ui = UI()
        with patch("builtins.input", return_value="2 3"):
            row, col = ui.get_move("Игрок 1")
            assert (row, col) == (1, 2)

    def test_ui_get_move_retry_on_invalid(self):
        """При неверном вводе запрашивает координаты повторно."""
        ui = UI()
        with patch("builtins.input", side_effect=["err", "4 4", "1 1"]):
            with patch.object(ui, "show_message") as mock_show:
                row, col = ui.get_move("Игрок 1")
                assert (row, col) == (0, 0)
                assert mock_show.call_count == 2
