"""Тесты для протоколов способностей."""

from core.protocols import Movable, Drawable, Collidable


class TestProtocols:
    def test_object_with_draw_is_drawable(self):
        """Объект с методом draw проходит isinstance(obj, Drawable)."""
        class Visual:
            def draw(self) -> str:
                return "вид"

        assert isinstance(Visual(), Drawable)

    def test_object_without_draw_is_not_drawable(self):
        """Объект без метода draw не является Drawable."""
        class NonVisual:
            pass

        assert not isinstance(NonVisual(), Drawable)

    def test_object_with_move_is_movable(self):
        """Объект с методом move проходит isinstance(obj, Movable)."""
        class Unit:
            def move(self, dx: float, dy: float) -> None:
                pass

        assert isinstance(Unit(), Movable)

    def test_object_with_collision_is_collidable(self):
        """Объект с радиусом и методом collides_with проходит Collidable."""
        class Barrier:
            @property
            def collision_radius(self) -> float:
                return 1.5

            def collides_with(self, other: Collidable) -> bool:
                return True

        assert isinstance(Barrier(), Collidable)

    def test_int_is_not_drawable(self):
        """Примитивные типы не удовлетворяют протоколам."""
        assert not isinstance(42, Drawable)
