"""Тесты класса Board."""
from src.board import Board


class TestBoard:
    """Проверяем механику и правила игрового поля."""

    def test_initial_board_empty(self):
        """Новое поле должно быть пустым и не заполненным."""
        board = Board()
        assert not board.is_full()
        assert board.check_winner() is None

    def test_make_move_success(self):
        """Ход в свободную клетку должен проходить успешно."""
        board = Board()
        assert board.make_move(0, 0, "X") is True
        assert board.get_grid()[0][0] == "X"

    def test_make_move_occupied_cell(self):
        """Ход в уже занятую клетку должен отклоняться."""
        board = Board()
        board.make_move(1, 1, "X")
        assert board.make_move(1, 1, "O") is False
        assert board.get_grid()[1][1] == "X"

    def test_check_winner_horizontal(self):
        """Проверка победы по горизонтальной линии."""
        board = Board()
        for col in range(3):
            board.make_move(0, col, "X")
        assert board.check_winner() == "X"

    def test_check_winner_diagonal(self):
        """Проверка победы по диагонали."""
        board = Board()
        board.make_move(0, 0, "O")
        board.make_move(1, 1, "O")
        board.make_move(2, 2, "O")
        assert board.check_winner() == "O"

    def test_is_full_draw(self):
        """Проверка полного заполнения поля без победителя (ничья)."""
        board = Board()
        moves = [
            (0, 0, "X"), (0, 1, "O"), (0, 2, "X"),
            (1, 0, "X"), (1, 1, "O"), (1, 2, "O"),
            (2, 0, "O"), (2, 1, "X"), (2, 2, "X"),
        ]
        for r, c, s in moves:
            board.make_move(r, c, s)
        assert board.is_full() is True
        assert board.check_winner() is None
