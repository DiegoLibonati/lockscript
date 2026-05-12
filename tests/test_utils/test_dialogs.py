from typing import Any
from unittest.mock import MagicMock, patch

import pytest

from src.constants.messages import MESSAGE_ERROR_APP, MESSAGE_NOT_FOUND_DIALOG_TYPE
from src.utils.dialogs import (
    AuthenticationDialogError,
    BaseDialog,
    BaseDialogError,
    BaseDialogNotification,
    BusinessDialogError,
    ConflictDialogError,
    DeprecatedDialogWarning,
    InternalDialogError,
    NotFoundDialogError,
    SuccessDialogInformation,
    ValidationDialogError,
)


class TestBaseDialog:
    def test_dialog_type_default_is_error(self) -> None:
        dialog: BaseDialog = BaseDialog()

        assert dialog.dialog_type == BaseDialog.ERROR

    def test_message_default_is_error_app(self) -> None:
        dialog: BaseDialog = BaseDialog()

        assert dialog.message == MESSAGE_ERROR_APP

    def test_message_is_overridden_via_constructor(self) -> None:
        dialog: BaseDialog = BaseDialog(message="custom message")

        assert dialog.message == "custom message"

    def test_message_is_not_overridden_when_none_is_passed(self) -> None:
        dialog: BaseDialog = BaseDialog(message=None)

        assert dialog.message == MESSAGE_ERROR_APP

    def test_title_returns_error_for_error_dialog_type(self) -> None:
        dialog: BaseDialog = BaseDialog()

        assert dialog.title == "Error"

    def test_title_returns_warning_for_warning_dialog_type(self) -> None:
        class WarningDialog(BaseDialog):
            dialog_type = BaseDialog.WARNING

        assert WarningDialog().title == "Warning"

    def test_title_returns_information_for_info_dialog_type(self) -> None:
        class InfoDialog(BaseDialog):
            dialog_type = BaseDialog.INFO

        assert InfoDialog().title == "Information"

    def test_to_dict_contains_dialog_type_key(self) -> None:
        result: dict[str, Any] = BaseDialog().to_dict()

        assert "dialog_type" in result

    def test_to_dict_contains_title_key(self) -> None:
        result: dict[str, Any] = BaseDialog().to_dict()

        assert "title" in result

    def test_to_dict_contains_message_key(self) -> None:
        result: dict[str, Any] = BaseDialog().to_dict()

        assert "message" in result

    def test_to_dict_values_match_instance_state(self) -> None:
        dialog: BaseDialog = BaseDialog(message="test-msg")

        result: dict[str, Any] = dialog.to_dict()

        assert result["dialog_type"] == BaseDialog.ERROR
        assert result["title"] == "Error"
        assert result["message"] == "test-msg"

    def test_open_calls_showerror_for_error_type(self) -> None:
        dialog: BaseDialog = BaseDialog()
        mock_handler: MagicMock = MagicMock()

        with patch.dict(BaseDialog._HANDLERS, {BaseDialog.ERROR: mock_handler}):
            dialog.open()

        mock_handler.assert_called_once_with("Error", MESSAGE_ERROR_APP)

    def test_open_calls_showwarning_for_warning_type(self) -> None:
        class WarningDialog(BaseDialog):
            dialog_type = BaseDialog.WARNING
            message = "warn-msg"

        mock_handler: MagicMock = MagicMock()

        with patch.dict(BaseDialog._HANDLERS, {BaseDialog.WARNING: mock_handler}):
            WarningDialog().open()

        mock_handler.assert_called_once_with("Warning", "warn-msg")

    def test_open_calls_showinfo_for_info_type(self) -> None:
        class InfoDialog(BaseDialog):
            dialog_type = BaseDialog.INFO
            message = "info-msg"

        mock_handler: MagicMock = MagicMock()

        with patch.dict(BaseDialog._HANDLERS, {BaseDialog.INFO: mock_handler}):
            InfoDialog().open()

        mock_handler.assert_called_once_with("Information", "info-msg")

    def test_open_calls_showerror_when_dialog_type_is_invalid(self) -> None:
        class BadDialog(BaseDialog):
            dialog_type = "INVALID"

        with patch("src.utils.dialogs.messagebox.showerror") as mock_showerror:
            BadDialog().open()

            mock_showerror.assert_called_once_with(BaseDialog.ERROR, MESSAGE_NOT_FOUND_DIALOG_TYPE)


class TestBaseDialogError:
    def test_is_subclass_of_exception(self) -> None:
        assert issubclass(BaseDialogError, Exception)

    def test_is_subclass_of_base_dialog(self) -> None:
        assert issubclass(BaseDialogError, BaseDialog)

    def test_dialog_type_is_error(self) -> None:
        assert BaseDialogError.dialog_type == BaseDialog.ERROR

    def test_can_be_raised_and_caught(self) -> None:
        with pytest.raises(BaseDialogError):
            raise BaseDialogError()


class TestValidationDialogError:
    def test_is_subclass_of_base_dialog_error(self) -> None:
        assert issubclass(ValidationDialogError, BaseDialogError)

    def test_can_be_raised_and_caught(self) -> None:
        with pytest.raises(ValidationDialogError):
            raise ValidationDialogError()

    def test_is_caught_as_base_dialog_error(self) -> None:
        with pytest.raises(BaseDialogError):
            raise ValidationDialogError()

    def test_message_can_be_set_via_constructor(self) -> None:
        error: ValidationDialogError = ValidationDialogError(message="invalid input")

        assert error.message == "invalid input"


class TestAuthenticationDialogError:
    def test_is_subclass_of_base_dialog_error(self) -> None:
        assert issubclass(AuthenticationDialogError, BaseDialogError)

    def test_can_be_raised_and_caught(self) -> None:
        with pytest.raises(AuthenticationDialogError):
            raise AuthenticationDialogError()


class TestNotFoundDialogError:
    def test_is_subclass_of_base_dialog_error(self) -> None:
        assert issubclass(NotFoundDialogError, BaseDialogError)

    def test_can_be_raised_and_caught(self) -> None:
        with pytest.raises(NotFoundDialogError):
            raise NotFoundDialogError()


class TestConflictDialogError:
    def test_is_subclass_of_base_dialog_error(self) -> None:
        assert issubclass(ConflictDialogError, BaseDialogError)

    def test_can_be_raised_and_caught(self) -> None:
        with pytest.raises(ConflictDialogError):
            raise ConflictDialogError()


class TestBusinessDialogError:
    def test_is_subclass_of_base_dialog_error(self) -> None:
        assert issubclass(BusinessDialogError, BaseDialogError)

    def test_can_be_raised_and_caught(self) -> None:
        with pytest.raises(BusinessDialogError):
            raise BusinessDialogError()


class TestInternalDialogError:
    def test_is_subclass_of_base_dialog_error(self) -> None:
        assert issubclass(InternalDialogError, BaseDialogError)

    def test_message_can_be_set_via_constructor(self) -> None:
        error: InternalDialogError = InternalDialogError(message="internal failure")

        assert error.message == "internal failure"

    def test_can_be_raised_and_caught(self) -> None:
        with pytest.raises(InternalDialogError):
            raise InternalDialogError()


class TestBaseDialogNotification:
    def test_is_subclass_of_base_dialog(self) -> None:
        assert issubclass(BaseDialogNotification, BaseDialog)

    def test_is_not_an_exception(self) -> None:
        assert not issubclass(BaseDialogNotification, Exception)


class TestDeprecatedDialogWarning:
    def test_is_subclass_of_base_dialog_notification(self) -> None:
        assert issubclass(DeprecatedDialogWarning, BaseDialogNotification)

    def test_dialog_type_is_warning(self) -> None:
        assert DeprecatedDialogWarning.dialog_type == BaseDialog.WARNING


class TestSuccessDialogInformation:
    def test_is_subclass_of_base_dialog_notification(self) -> None:
        assert issubclass(SuccessDialogInformation, BaseDialogNotification)

    def test_dialog_type_is_info(self) -> None:
        assert SuccessDialogInformation.dialog_type == BaseDialog.INFO

    def test_can_be_instantiated(self) -> None:
        notification: SuccessDialogInformation = SuccessDialogInformation()

        assert notification is not None
