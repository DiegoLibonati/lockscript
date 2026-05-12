import logging

from src.configs.logger_config import setup_logger


class TestSetupLogger:
    def test_returns_logger_instance(self) -> None:
        logger: logging.Logger = setup_logger()

        assert isinstance(logger, logging.Logger)

    def test_default_name_is_tkinter_app(self) -> None:
        logger: logging.Logger = setup_logger()

        assert logger.name == "tkinter-app"

    def test_custom_name_is_used(self) -> None:
        logger: logging.Logger = setup_logger("custom-logger-name")

        assert logger.name == "custom-logger-name"

    def test_logger_has_handlers_after_setup(self) -> None:
        logger: logging.Logger = setup_logger("test-logger-with-handlers")

        assert len(logger.handlers) > 0

    def test_calling_twice_does_not_add_extra_handlers(self) -> None:
        logger: logging.Logger = setup_logger("test-logger-idempotent")
        initial_count: int = len(logger.handlers)

        setup_logger("test-logger-idempotent")

        assert len(logger.handlers) == initial_count

    def test_logger_level_is_debug(self) -> None:
        logger: logging.Logger = setup_logger("test-logger-level")

        assert logger.level == logging.DEBUG
