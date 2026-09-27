"""Главный менеджер игры Крестики-нолики."""

from .board import Board
from .player import Player
from .ui import UI


class Game:
    """Управляет жизненным циклом партии и очередностью ходов."""

    def __init__(self, ui: UI | None = None) -> None:
        self._ui = ui if ui is not None else UI()
        self._board = Board()
        self._players = [
            Player("Игрок 1", "X"),
            Player("Игрок 2", "O")
        ]
        self._current_index = 0

    @property
    def current_player(self) -> Player:
        return self._players[self._current_index]

    def _switch_player(self) -> None:
        self._current_index = 1 - self._current_index

    def run(self) -> None:
        """Запустить основной цикл игры."""
        self._ui.show_message("Добро пожаловать в игру Крестики-нолики!")

        while True:
            self._ui.display_board(self._board.get_grid())
            player = self.current_player

            while True:
                row, col = self._ui.get_move(player.name)
                if self._board.make_move(row, col, player.symbol):
                    break
                self._ui.show_message("Клетка уже занята! Выберите другую.")

            winner = self._board.check_winner()
            if winner:
                self._ui.display_board(self._board.get_grid())
                msg = f"Победил {player.name} ({winner})! Поздравляем!"
                self._ui.show_message(msg)
                return

            if self._board.is_full():
                self._ui.display_board(self._board.get_grid())
                self._ui.show_message("Ничья! Победила дружба.")
                return

            self._switch_player()
