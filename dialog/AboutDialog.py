from PySide6.QtWidgets import QDialog

from dialog.about_dlg import Ui_AboutDialog


class AboutDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui_dialog = Ui_AboutDialog()
        self.ui_dialog.setupUi(self)
        self.setWindowTitle(u"关于")
