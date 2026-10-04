"""Тесты для LoggingMixin."""

from core.mixins import LoggingMixin


class TestLoggingMixin:
    def test_log_methods_work(self):
        """Методы логирования вызываются без ошибок на любом классе."""
        class Service(LoggingMixin):
            pass

        srv = Service()
        srv.log("Информационное сообщение")
        srv.log_warning("Предупреждение")
        srv.log_error("Ошибка")

    def test_mixin_has_no_state(self):
        """Миксин не имеет собственного состояния (__slots__ = ())."""
        assert LoggingMixin.__slots__ == ()
