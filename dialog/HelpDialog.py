from PySide6.QtWidgets import QDialog

from dialog.help_dlg import Ui_HelpDialog


class HelpDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui_dialog = Ui_HelpDialog()
        self.ui_dialog.setupUi(self)
        self.setWindowTitle(u"帮助")
