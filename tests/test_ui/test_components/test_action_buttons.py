import tkinter as tk
from unittest.mock import MagicMock

from src.ui.components.action_buttons import ActionButtons
from src.ui.styles import Styles


class TestActionButtons:
    def test_instantiation(self, root: tk.Tk) -> None:
        buttons: ActionButtons = ActionButtons(root, Styles(), MagicMock(), MagicMock())

        assert buttons is not None
        buttons.destroy()

    def test_has_two_child_buttons(self, root: tk.Tk) -> None:
        buttons: ActionButtons = ActionButtons(root, Styles(), MagicMock(), MagicMock())

        children: list[tk.Widget] = buttons.winfo_children()

        assert len(children) == 2
        buttons.destroy()

    def test_encrypt_button_invokes_encrypt_callback(self, root: tk.Tk) -> None:
        mock_encrypt: MagicMock = MagicMock()
        buttons: ActionButtons = ActionButtons(root, Styles(), mock_encrypt, MagicMock())

        encrypt_btn: tk.Button = buttons.winfo_children()[0]
        encrypt_btn.invoke()

        mock_encrypt.assert_called_once()
        buttons.destroy()

    def test_decrypt_button_invokes_decrypt_callback(self, root: tk.Tk) -> None:
        mock_decrypt: MagicMock = MagicMock()
        buttons: ActionButtons = ActionButtons(root, Styles(), MagicMock(), mock_decrypt)

        decrypt_btn: tk.Button = buttons.winfo_children()[1]
        decrypt_btn.invoke()

        mock_decrypt.assert_called_once()
        buttons.destroy()

    def test_encrypt_callback_is_not_called_on_decrypt_invoke(self, root: tk.Tk) -> None:
        mock_encrypt: MagicMock = MagicMock()
        buttons: ActionButtons = ActionButtons(root, Styles(), mock_encrypt, MagicMock())

        decrypt_btn: tk.Button = buttons.winfo_children()[1]
        decrypt_btn.invoke()

        mock_encrypt.assert_not_called()
        buttons.destroy()

    def test_decrypt_callback_is_not_called_on_encrypt_invoke(self, root: tk.Tk) -> None:
        mock_decrypt: MagicMock = MagicMock()
        buttons: ActionButtons = ActionButtons(root, Styles(), MagicMock(), mock_decrypt)

        encrypt_btn: tk.Button = buttons.winfo_children()[0]
        encrypt_btn.invoke()

        mock_decrypt.assert_not_called()
        buttons.destroy()
