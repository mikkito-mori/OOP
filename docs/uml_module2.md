# Архитектурная модель: Модуль 2

## UML-диаграмма классов

```mermaid
classDiagram
    class GameObject {
        <<abstract>>
        -_id: int
        -_name: str
        -_active: bool
        +id: int
        +name: str
        +active: bool
        +deactivate() void
        +update(dt: float)* void
        +draw()* str
    }

    class Movable {
        <<protocol>>
        +move(dx: float, dy: float) void
    }

    class Drawable {
        <<protocol>>
        +draw() str
    }

    class Collidable {
        <<protocol>>
        +collision_radius: float
        +collides_with(other) bool
    }

    class LoggingMixin {
        +log(message: str) void
        +log_warning(message: str) void
        +log_error(message: str) void
    }

    class Board {
        -_size: int
        -_grid: list
        +update(dt: float) void
        +draw() str
        +place_mark(x: int, y: int, mark: str) bool
    }

    class Player {
        -_symbol: str
        +update(dt: float) void
        +draw() str
        +move(dx: float, dy: float) void
    }

    LoggingMixin <|-- Board
    GameObject <|-- Board
    Drawable <|.. Board : implements

    LoggingMixin <|-- Player
    GameObject <|-- Player
    Drawable <|.. Player : implements
    Movable <|.. Player : implements
```

## Ответы на вопросы проектирования

1. **Почему `GameObject` - это ABC, а не Protocol?**
   `GameObject` задает фундаментальную сущность (<чем объект является>) и содержит общее состояние и реализацию: инкремент `_id`, хранение имени `_name`, флага активности `_active` и метод `deactivate()`. Протоколы не должны навязывать конкретную базовую реализацию состояния.
2. **Почему `Movable` - это Protocol, а не ABC?**
   `Movable` определяет исключительно роль/поведение (<что объект умеет делать>). Использование протокола позволяет проверять поддержку перемещения через структурную типизацию (<утиная типизация>) без жесткой привязки к дереву наследования.
3. **Какие классы реализуют несколько протоколов одновременно?**
   Класс `Player` реализует одновременно `Drawable` (может отображаться в интерфейсе со своим символом и статистикой) и `Movable` (выполняет ход с изменением координат).
4. **Какие классы не должны наследоваться от `GameObject`?**
   Классы `UI`, `Game` (оркестратор игрового процесса) и конфигурационные датаклассы (`GameConfig`, `PlayerConfig`). Они не являются объектами игрового мира, а представляют собой внешние сервисы и структуры данных.
