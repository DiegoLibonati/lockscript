import sys
from unittest.mock import MagicMock, patch

from src.utils.dialogs import InternalDialogError, ValidationDialogError
from src.utils.tkinter_exception_hook import tkinter_exception_hook


class TestTkinterExceptionHook:
    def test_calls_open_on_base_dialog_exception(self) -> None:
        try:
            raise ValidationDialogError(message="invalid")
        except ValidationDialogError:
            exc_type, exc_value, exc_tb = sys.exc_info()

        with patch.object(exc_value, "open") as mock_open:
            tkinter_exception_hook(exc_type, exc_value, exc_tb)

            mock_open.assert_called_once()

    def test_calls_internal_dialog_error_open_for_generic_exception(self) -> None:
        try:
            raise Exception("something went wrong")
        except Exception:
            exc_type, exc_value, exc_tb = sys.exc_info()

        with patch("src.utils.tkinter_exception_hook.InternalDialogError") as mock_cls:
            mock_instance: MagicMock = MagicMock()
            mock_cls.return_value = mock_instance

            tkinter_exception_hook(exc_type, exc_value, exc_tb)

            mock_cls.assert_called_once_with(message="something went wrong")
            mock_instance.open.assert_called_once()

    def test_does_not_wrap_base_dialog_in_internal_error(self) -> None:
        try:
            raise ValidationDialogError(message="validation failed")
        except ValidationDialogError:
            exc_type, exc_value, exc_tb = sys.exc_info()

        with patch("src.utils.tkinter_exception_hook.InternalDialogError") as mock_internal:
            with patch.object(exc_value, "open"):
                tkinter_exception_hook(exc_type, exc_value, exc_tb)

                mock_internal.assert_not_called()

    def test_logs_error_for_any_exception(self) -> None:
        try:
            raise Exception("test error")
        except Exception:
            exc_type, exc_value, exc_tb = sys.exc_info()

        with patch("src.utils.tkinter_exception_hook.logger") as mock_logger:
            with patch("src.utils.tkinter_exception_hook.InternalDialogError"):
                tkinter_exception_hook(exc_type, exc_value, exc_tb)

                mock_logger.error.assert_called_once()

    def test_logs_error_for_base_dialog_exception(self) -> None:
        try:
            raise InternalDialogError(message="internal")
        except InternalDialogError:
            exc_type, exc_value, exc_tb = sys.exc_info()

        with patch("src.utils.tkinter_exception_hook.logger") as mock_logger:
            with patch.object(exc_value, "open"):
                tkinter_exception_hook(exc_type, exc_value, exc_tb)

                mock_logger.error.assert_called_once()
