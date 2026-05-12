import tkinter as tk
from unittest.mock import MagicMock, patch

from src.configs.development_config import DevelopmentConfig
from src.constants.messages import MESSAGE_SUCCESS_DECRYPTED, MESSAGE_SUCCESS_ENCRYPTED
from src.ui.interface_app import InterfaceApp


class TestInterfaceApp:
    def test_instantiation(self, root: tk.Tk) -> None:
        app: InterfaceApp = InterfaceApp(root, DevelopmentConfig())

        assert app is not None
        app._main_view.destroy()

    def test_title_is_lockscript(self, root: tk.Tk) -> None:
        app: InterfaceApp = InterfaceApp(root, DevelopmentConfig())

        assert root.title() == "Lockscript"
        app._main_view.destroy()

    def test_initial_path_is_empty_string(self, root: tk.Tk) -> None:
        app: InterfaceApp = InterfaceApp(root, DevelopmentConfig())

        assert app._path == ""
        app._main_view.destroy()

    def test_select_file_updates_path(self, root: tk.Tk) -> None:
        app: InterfaceApp = InterfaceApp(root, DevelopmentConfig())

        with patch("src.ui.interface_app.filedialog.askopenfilename") as mock_dialog:
            mock_dialog.return_value = "/path/to/file.txt"

            app._select_file()

        assert app._path == "/path/to/file.txt"
        app._main_view.destroy()

    def test_select_file_updates_import_label(self, root: tk.Tk) -> None:
        app: InterfaceApp = InterfaceApp(root, DevelopmentConfig())

        with patch("src.ui.interface_app.filedialog.askopenfilename") as mock_dialog:
            mock_dialog.return_value = "/path/to/file.txt"

            app._select_file()

        assert app._main_view._file_importer._label_import_file.get() == "/path/to/file.txt"
        app._main_view.destroy()

    def test_encrypt_file_calls_file_service_with_current_path(self, root: tk.Tk) -> None:
        app: InterfaceApp = InterfaceApp(root, DevelopmentConfig())
        app._path = "/path/to/file.txt"

        with patch("src.ui.interface_app.FileService") as mock_service_cls:
            mock_service: MagicMock = MagicMock()
            mock_service_cls.return_value = mock_service
            mock_service.encrypt_file.return_value = True

            app._encrypt_file()

            mock_service.encrypt_file.assert_called_once_with(filepath="/path/to/file.txt")
        app._main_view.destroy()

    def test_encrypt_file_sets_success_result_on_ok(self, root: tk.Tk) -> None:
        app: InterfaceApp = InterfaceApp(root, DevelopmentConfig())
        app._path = "/path/to/file.txt"

        with patch("src.ui.interface_app.FileService") as mock_service_cls:
            mock_service: MagicMock = MagicMock()
            mock_service_cls.return_value = mock_service
            mock_service.encrypt_file.return_value = True

            app._encrypt_file()

        assert app._main_view._label_operation_result.get() == MESSAGE_SUCCESS_ENCRYPTED
        app._main_view.destroy()

    def test_encrypt_file_does_not_set_result_when_service_returns_false(self, root: tk.Tk) -> None:
        app: InterfaceApp = InterfaceApp(root, DevelopmentConfig())

        with patch("src.ui.interface_app.FileService") as mock_service_cls:
            mock_service: MagicMock = MagicMock()
            mock_service_cls.return_value = mock_service
            mock_service.encrypt_file.return_value = False

            app._encrypt_file()

        assert app._main_view._label_operation_result.get() == ""
        app._main_view.destroy()

    def test_decrypt_file_calls_file_service_with_current_path(self, root: tk.Tk) -> None:
        app: InterfaceApp = InterfaceApp(root, DevelopmentConfig())
        app._path = "/path/to/file.txt"

        with patch("src.ui.interface_app.FileService") as mock_service_cls:
            mock_service: MagicMock = MagicMock()
            mock_service_cls.return_value = mock_service
            mock_service.decrypt_file.return_value = True

            app._decrypt_file()

            mock_service.decrypt_file.assert_called_once_with(filepath="/path/to/file.txt")
        app._main_view.destroy()

    def test_decrypt_file_sets_success_result_on_ok(self, root: tk.Tk) -> None:
        app: InterfaceApp = InterfaceApp(root, DevelopmentConfig())
        app._path = "/path/to/file.txt"

        with patch("src.ui.interface_app.FileService") as mock_service_cls:
            mock_service: MagicMock = MagicMock()
            mock_service_cls.return_value = mock_service
            mock_service.decrypt_file.return_value = True

            app._decrypt_file()

        assert app._main_view._label_operation_result.get() == MESSAGE_SUCCESS_DECRYPTED
        app._main_view.destroy()

    def test_decrypt_file_does_not_set_result_when_service_returns_false(self, root: tk.Tk) -> None:
        app: InterfaceApp = InterfaceApp(root, DevelopmentConfig())

        with patch("src.ui.interface_app.FileService") as mock_service_cls:
            mock_service: MagicMock = MagicMock()
            mock_service_cls.return_value = mock_service
            mock_service.decrypt_file.return_value = False

            app._decrypt_file()

        assert app._main_view._label_operation_result.get() == ""
        app._main_view.destroy()
