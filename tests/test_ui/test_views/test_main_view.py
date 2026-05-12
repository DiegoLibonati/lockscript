import tkinter as tk
from unittest.mock import MagicMock

from src.ui.styles import Styles
from src.ui.views.main_view import MainView


class TestMainView:
    def test_instantiation(self, root: tk.Tk) -> None:
        view: MainView = MainView(
            root=root,
            styles=Styles(),
            on_import=MagicMock(),
            on_encrypt=MagicMock(),
            on_decrypt=MagicMock(),
        )

        assert view is not None
        view.destroy()

    def test_result_label_is_empty_on_init(self, root: tk.Tk) -> None:
        view: MainView = MainView(
            root=root,
            styles=Styles(),
            on_import=MagicMock(),
            on_encrypt=MagicMock(),
            on_decrypt=MagicMock(),
        )

        assert view._label_operation_result.get() == ""
        view.destroy()

    def test_set_result_updates_label_variable(self, root: tk.Tk) -> None:
        view: MainView = MainView(
            root=root,
            styles=Styles(),
            on_import=MagicMock(),
            on_encrypt=MagicMock(),
            on_decrypt=MagicMock(),
        )

        view.set_result("Successfully encrypted.")

        assert view._label_operation_result.get() == "Successfully encrypted."
        view.destroy()

    def test_set_result_with_empty_string_clears_label(self, root: tk.Tk) -> None:
        view: MainView = MainView(
            root=root,
            styles=Styles(),
            on_import=MagicMock(),
            on_encrypt=MagicMock(),
            on_decrypt=MagicMock(),
        )
        view.set_result("initial text")

        view.set_result("")

        assert view._label_operation_result.get() == ""
        view.destroy()

    def test_set_import_label_delegates_to_file_importer(self, root: tk.Tk) -> None:
        view: MainView = MainView(
            root=root,
            styles=Styles(),
            on_import=MagicMock(),
            on_encrypt=MagicMock(),
            on_decrypt=MagicMock(),
        )

        view.set_import_label("/some/path.txt")

        assert view._file_importer._label_import_file.get() == "/some/path.txt"
        view.destroy()
