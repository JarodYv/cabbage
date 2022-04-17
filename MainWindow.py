from PySide6 import QtGui, QtCore

from dialog.SettingDialog import SettingDialog
from main_window import Ui_MainWindow
from dialog.AboutDialog import AboutDialog
from dialog.HelpDialog import HelpDialog
from PySide6.QtWidgets import QMainWindow, QListWidgetItem
from PySide6.QtCore import Qt
from core.device import get_device_list
from widget.DeviceWidget import DeviceWidget


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.current_page = None
        self.last_page = None
        self.ui.btn_tutor.clicked.connect(
            lambda: QtGui.QDesktopServices.openUrl(QtCore.QUrl('https://cabbage.planplus.cn')))
        self.ui.btn_home.clicked.connect(self.back2home)
        self.ui.btn_setting.clicked.connect(lambda: SettingDialog().exec())
        self.ui.btn_about.clicked.connect(lambda: AboutDialog().exec())
        self.ui.btn_init.clicked.connect(self.init_device)
        self.ui.listWidget.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.back2home()

    def back2home(self):
        self.ui.listWidget.clear()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.btn_home.hide()

    def init_device(self):
        devices = get_device_list()
        if devices:
            for device in devices:
                device_widget = DeviceWidget(self, device["product"], device["device_id"])
                item = QListWidgetItem()
                # item.setSizeHint(device_widget.sizeHint())
                self.ui.listWidget.addItem(item)
                self.ui.listWidget.setItemWidget(item, device_widget)
            self.ui.stackedWidget.setCurrentIndex(1)
            self.ui.btn_home.show()
        else:
            HelpDialog().exec()

    # def resizeEvent(self, event):
    #     self.overlay.resize(event.size())
    #     event.accept()
