"""Тесты для ABC GameObject."""

import pytest
from core.game_object import GameObject


class TestGameObjectABC:
    def test_cannot_instantiate_abstract(self):
        """ABC нельзя создать напрямую."""
        with pytest.raises(TypeError):
            GameObject("test")

    def test_subclass_must_implement_methods(self):
        """Подкласс без update/draw нельзя создать."""
        class Incomplete(GameObject):
            pass

        with pytest.raises(TypeError):
            Incomplete("test")

    def test_concrete_subclass_works(self):
        """Полный подкласс создаётся и работает."""
        class Concrete(GameObject):
            def update(self, dt: float) -> None:
                pass

            def draw(self) -> str:
                return "Concrete"

        obj = Concrete("Объект 1")
        assert obj.name == "Объект 1"
        assert isinstance(obj.id, int)
        assert obj.active is True

    def test_unique_ids(self):
        # Базовая проверка счетчика id
        class Concrete(GameObject):
            def update(self, dt: float) -> None:
                pass

            def draw(self) -> str:
                return "Concrete"

        a = Concrete("A")
        b = Concrete("B")
        assert a.id != b.id

    def test_deactivate(self):
        """После вызова deactivate() объект становится неактивным."""
        class Concrete(GameObject):
            def update(self, dt: float) -> None:
                pass

            def draw(self) -> str:
                return "Concrete"

        obj = Concrete("Тест")
        obj.deactivate()
        assert obj.active is False
