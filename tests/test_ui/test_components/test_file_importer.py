import tkinter as tk
from unittest.mock import MagicMock

from src.ui.components.file_importer import FileImporter
from src.ui.styles import Styles


class TestFileImporter:
    def test_instantiation(self, root: tk.Tk) -> None:
        importer: FileImporter = FileImporter(root, Styles(), MagicMock())

        assert importer is not None
        importer.destroy()

    def test_initial_path_label_is_empty(self, root: tk.Tk) -> None:
        importer: FileImporter = FileImporter(root, Styles(), MagicMock())

        assert importer._label_import_file.get() == ""
        importer.destroy()

    def test_set_path_updates_label_variable(self, root: tk.Tk) -> None:
        importer: FileImporter = FileImporter(root, Styles(), MagicMock())

        importer.set_path("/some/path/file.txt")

        assert importer._label_import_file.get() == "/some/path/file.txt"
        importer.destroy()

    def test_set_path_with_empty_string_clears_label(self, root: tk.Tk) -> None:
        importer: FileImporter = FileImporter(root, Styles(), MagicMock())
        importer.set_path("/initial/path.txt")

        importer.set_path("")

        assert importer._label_import_file.get() == ""
        importer.destroy()

    def test_import_button_invokes_callback(self, root: tk.Tk) -> None:
        mock_import: MagicMock = MagicMock()
        importer: FileImporter = FileImporter(root, Styles(), mock_import)

        import_btn: tk.Button = importer.winfo_children()[0]
        import_btn.invoke()

        mock_import.assert_called_once()
        importer.destroy()
