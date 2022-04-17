from PySide6.QtCore import QSettings
from PySide6.QtWidgets import QDialog

from dialog.setting import Ui_SettingDialog


class SettingDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui_dialog = Ui_SettingDialog()
        self.ui_dialog.setupUi(self)
        self.setWindowTitle(u"设置")
        self.config = QSettings('config.ini', QSettings.IniFormat)
        op_time = self.config.value("op_time", 0)
        err_time = self.config.value("err_time", 5)
        is_play_sound = self.config.value("play_sound", 1)
        self.ui_dialog.op_time.setValue(int(op_time))
        self.ui_dialog.err_time.setValue(int(err_time))
        self.ui_dialog.play_sound.setChecked(int(is_play_sound) == 1)

    def accept(self):
        op_time = self.ui_dialog.op_time.value()
        err_time = self.ui_dialog.err_time.value()
        is_play_sound = 1 if self.ui_dialog.play_sound.isChecked() else 0
        self.config.setValue("op_time", op_time)
        self.config.setValue("err_time", err_time)
        self.config.setValue("play_sound", is_play_sound)
        super(SettingDialog, self).accept()
