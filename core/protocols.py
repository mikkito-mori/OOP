"""Протоколы способностей игровых сущностей."""

from typing import Protocol, runtime_checkable


@runtime_checkable
class Movable(Protocol):
    """Роль: объект умеет перемещаться или совершать ход."""
    def move(self, dx: float, dy: float) -> None:
        ...


@runtime_checkable
class Drawable(Protocol):
    """Роль: объект можно отрисовать или отобразить."""
    def draw(self) -> str:
        ...


@runtime_checkable
class Collidable(Protocol):
    """Роль: объект может участвовать в проверке пересечений/коллизий."""
    @property
    def collision_radius(self) -> float:
        ...

    def collides_with(self, other: "Collidable") -> bool:
        ...
