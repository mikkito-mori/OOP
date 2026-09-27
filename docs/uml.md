```mermaid
classDiagram
    class Board {
        -_grid: list
        +make_move(row: int, col: int, symbol: str) bool
        +is_valid_move(row: int, col: int) bool
        +check_winner() str
        +is_full() bool
        +get_grid() list
    }

    class Player {
        -_name: str
        -_symbol: str
        +name: str
        +symbol: str
    }

    class UI {
        +display_board(grid: list) void
        +get_move(player_name: str) tuple
        +show_message(message: str) void
    }

    class Game {
        -_board: Board
        -_players: list
        -_current_index: int
        -_ui: UI
        +run() void
        -_switch_player() void
    }

    Game --> Board : creates
    Game --> Player : creates
    Game --> UI : uses
```
