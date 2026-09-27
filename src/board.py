"""Модуль игрового поля."""

from core.game_object import GameObject
from core.mixins import LoggingMixin
from core.config import GameConfig, BoardConfig


class Board(LoggingMixin, GameObject):
    """Игровое поле для игры в крестики-нолики.

    Наследует GameObject и LoggingMixin.
    Реализует протокол Drawable.
    """

    def __init__(
        self,
        game_config: GameConfig | None = None,
        board_config: BoardConfig | None = None,
    ):
        super().__init__(name="Игровое поле")
        self._game_cfg = game_config if game_config else GameConfig()
        self._board_cfg = board_config if board_config else BoardConfig()
        self._size = self._game_cfg.grid_size
        empty = self._board_cfg.empty_cell
        # Инициализация пустой сетки
        self._grid = [[empty for _ in range(self._size)]
                      for _ in range(self._size)]
        self.log(f"Инициализировано поле размером {self._size}x{self._size}")

    @property
    def size(self) -> int:
        return self._size

    @property
    def grid(self) -> list[list[str]]:
        return self._grid

    def get_grid(self) -> list[list[str]]:
        """Возвращает текущую сетку поля (совместимость с модулем 1)."""
        return self._grid

    def make_move(self, row: int, col: int, symbol: str) -> bool:
        """Сделать ход в указанную клетку."""
        if not (0 <= row < self._size and 0 <= col < self._size):
            self.log_warning(f"Ход вне границ поля: ({row}, {col})")
            return False
        if self._grid[row][col] != self._board_cfg.empty_cell:
            msg = f"Попытка занять уже занятую ячейку: ({row}, {col})"
            self.log_warning(msg)
            return False

        self._grid[row][col] = symbol
        self._board_cfg.history.append((row, col, symbol))
        self.log(f"Ход {symbol} совершен в ячейку ({row}, {col})")
        return True

    def check_winner(self) -> str | None:
        """Проверка наличия победителя."""
        lines = []
        # Собираем строки и столбцы
        for i in range(self._size):
            lines.append(self._grid[i])
            lines.append([self._grid[j][i] for j in range(self._size)])

        # Главная и побочная диагонали
        lines.append([self._grid[i][i] for i in range(self._size)])
        anti_diag = [self._grid[i][self._size - 1 - i]
                     for i in range(self._size)]
        lines.append(anti_diag)

        win_len = self._game_cfg.win_length
        empty = self._board_cfg.empty_cell
        for line in lines:
            first = line[0]
            if first != empty and all(c == first for c in line[:win_len]):
                self.log(f"Победитель обнаружен: {first}")
                return first
        return None

    def is_full(self) -> bool:
        """Проверка, заполнено ли все поле."""
        empty = self._board_cfg.empty_cell
        return all(c != empty for row in self._grid for c in row)

    def update(self, dt: float) -> None:
        """Обновление состояния доски (контракт GameObject)."""
        # Пока обновлять нечего, логика статична
        pass

    def draw(self) -> str:
        """Отрисовка игрового поля в строку (контракт GameObject)."""
        rows = [" | ".join(row) for row in self._grid]
        sep = "\n" + "-" * (self._size * 4 - 3) + "\n"
        return sep.join(rows)
