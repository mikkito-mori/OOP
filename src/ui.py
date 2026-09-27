"""Модуль пользовательского интерфейса."""


class UI:
    """Отвечает за отображение данных и получение ввода от пользователя."""

    def show_message(self, message: str) -> None:
        """Вывести сообщение в консоль."""
        print(message)

    def display_board(self, grid: list) -> None:
        """Красиво отрисовать игровое поле 3x3."""
        print()
        for i, row in enumerate(grid):
            print(" " + " | ".join(row))
            if i < 2:
                print("---|---|---")
        print()

    def get_move(self, player_name: str) -> tuple[int, int]:
        """Запросить у игрока координаты клетки с валидацией."""
        prompt = f"{player_name}, введите строку и столбец (1-3): "
        while True:
            raw_input = input(prompt)
            parts = raw_input.strip().split()
            if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
                r, c = int(parts[0]) - 1, int(parts[1]) - 1
                if 0 <= r <= 2 and 0 <= c <= 2:
                    return r, c
            self.show_message("Ошибка: введите два числа от 1 до 3!")
