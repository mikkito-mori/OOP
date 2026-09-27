"""Модуль игрового поля."""


class Board:
    """Инкапсулирует сетку 3x3 и правила размещения символов."""

    def __init__(self) -> None:
        self._grid = [[" " for _ in range(3)] for _ in range(3)]

    def get_grid(self) -> list:
        """Получить текущую сетку поля."""
        return self._grid

    def is_valid_move(self, row: int, col: int) -> bool:
        """Проверить, свободна ли клетка."""
        return self._grid[row][col] == " "

    def make_move(self, row: int, col: int, symbol: str) -> bool:
        """Поставить символ в клетку, если она свободна."""
        if self.is_valid_move(row, col):
            self._grid[row][col] = symbol
            return True
        return False

    def is_full(self) -> bool:
        """Проверить, заполнено ли все поле."""
        return all(cell != " " for row in self._grid for cell in row)

    def check_winner(self) -> str | None:
        """Проверить победу. Возвращает "X", "O" или None."""
        lines = []
        for i in range(3):
            lines.append(self._grid[i])
            col = [self._grid[0][i], self._grid[1][i], self._grid[2][i]]
            lines.append(col)

        lines.append([self._grid[0][0], self._grid[1][1], self._grid[2][2]])
        lines.append([self._grid[0][2], self._grid[1][1], self._grid[2][0]])

        for line in lines:
            if line[0] != " " and line[0] == line[1] == line[2]:
                return line[0]
        return None
