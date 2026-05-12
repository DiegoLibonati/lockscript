import os
from pathlib import Path

import pytest

from src.services.file_service import FileService
from src.utils.dialogs import ValidationDialogError


class TestFileService:
    def test_base_path_defaults_to_empty_string(self) -> None:
        service: FileService = FileService()

        assert service.base_path == ""

    def test_base_path_is_set_when_provided(self) -> None:
        service: FileService = FileService(base_path="/some/path")

        assert service.base_path == "/some/path"

    def test_encrypt_raises_validation_error_when_path_is_empty(self) -> None:
        service: FileService = FileService()

        with pytest.raises(ValidationDialogError):
            service.encrypt_file(filepath="")

    def test_decrypt_raises_validation_error_when_path_is_empty(self) -> None:
        service: FileService = FileService()

        with pytest.raises(ValidationDialogError):
            service.decrypt_file(filepath="")

    def test_encrypt_raises_validation_error_when_not_txt(self) -> None:
        service: FileService = FileService()

        with pytest.raises(ValidationDialogError):
            service.encrypt_file(filepath="file.pdf")

    def test_decrypt_raises_validation_error_when_not_txt(self) -> None:
        service: FileService = FileService()

        with pytest.raises(ValidationDialogError):
            service.decrypt_file(filepath="file.pdf")

    def test_encrypt_file_returns_true_on_success(self, tmp_path: Path) -> None:
        test_file: Path = tmp_path / "test.txt"
        test_file.write_text("hello")
        service: FileService = FileService()

        result: bool = service.encrypt_file(filepath=str(test_file))

        assert result is True

    def test_decrypt_file_returns_true_on_success(self, tmp_path: Path) -> None:
        test_file: Path = tmp_path / "test.txt"
        test_file.write_text("ifmmp")
        service: FileService = FileService()

        result: bool = service.decrypt_file(filepath=str(test_file))

        assert result is True

    def test_encrypt_shifts_each_char_by_one(self, tmp_path: Path) -> None:
        test_file: Path = tmp_path / "test.txt"
        test_file.write_text("abc")
        service: FileService = FileService()

        service.encrypt_file(filepath=str(test_file))

        assert test_file.read_text() == "bcd"

    def test_decrypt_shifts_each_char_by_minus_one(self, tmp_path: Path) -> None:
        test_file: Path = tmp_path / "test.txt"
        test_file.write_text("bcd")
        service: FileService = FileService()

        service.decrypt_file(filepath=str(test_file))

        assert test_file.read_text() == "abc"

    def test_encrypt_then_decrypt_restores_original(self, tmp_path: Path) -> None:
        test_file: Path = tmp_path / "test.txt"
        original: str = "Hello, World!"
        test_file.write_text(original)
        service: FileService = FileService()

        service.encrypt_file(filepath=str(test_file))
        service.decrypt_file(filepath=str(test_file))

        assert test_file.read_text() == original

    def test_resolve_path_without_base_path(self) -> None:
        service: FileService = FileService()

        result: str = service._resolve_path(filepath="file.txt")

        assert result == "file.txt"

    def test_resolve_path_with_base_path(self) -> None:
        service: FileService = FileService(base_path="/base")

        result: str = service._resolve_path(filepath="file.txt")

        assert result == os.path.join("/base", "file.txt")

    def test_encrypt_with_base_path_resolves_full_path(self, tmp_path: Path) -> None:
        test_file: Path = tmp_path / "test.txt"
        test_file.write_text("abc")
        service: FileService = FileService(base_path=str(tmp_path))

        result: bool = service.encrypt_file(filepath="test.txt")

        assert result is True
        assert test_file.read_text() == "bcd"
