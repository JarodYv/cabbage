from PySide6.QtCore import QThread, QObject, Signal, Slot
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget

from core.dingdong import QiangDingdong
from core.meituan import QiangMeituan
from widget.device_widget import Ui_Device

from datetime import datetime

COLORS = ["#084298", "#0d6efd", "#198754", "#ffc107", "#dc3545"]


class DeviceWidget(QWidget):
    def __init__(self, parent, device_name: str, device_id: str):
        super(DeviceWidget, self).__init__(parent)
        self.device_name = device_name
        self.device_id = device_id
        self.ui = Ui_Device()
        self.ui.setupUi(self)
        self.ui.device_name.setText(self.device_name)
        self.ui.device_id.setText(self.device_id)
        self.ui.btn_run.clicked.connect(self.on_btn_clicked)
        self.is_running = False
        self.thread = None

    class ThreadSignal(QObject):
        progress = Signal(dict)

    class QCThread(QThread):
        def __init__(self, parent, device_id: str, is_dingdong: bool = True):
            super().__init__(parent)
            self.device_id = device_id
            self.is_dingdong = is_dingdong
            self.signal = DeviceWidget.ThreadSignal()
            self.qiang = None

        def run(self):
            if self.is_dingdong:
                self.qiang = QiangDingdong(self.signal.progress)
            else:
                self.qiang = QiangMeituan(self.signal.progress)
            self.qiang.run(self.device_id)

        def stop(self):
            if self.qiang:
                self.qiang.stop()
            self.wait()

    def on_btn_clicked(self):
        if self.thread and self.thread.isRunning():
            self.thread.stop()
            self.is_running = False
        else:
            self.is_running = True
            is_dingdong = self.ui.is_dingdong.isChecked()
            self.thread = DeviceWidget.QCThread(self, self.device_id, is_dingdong)
            self.thread.started.connect(lambda: self.on_thread_start())
            self.thread.signal.progress.connect(self.on_progress)
            self.thread.finished.connect(self.on_thread_finished)
            self.thread.start()

    def on_thread_finished(self):
        self.is_running = False
        self.append_log("抢菜程序停止")
        self.ui.is_dingdong.setEnabled(True)
        self.ui.is_meituan.setEnabled(True)
        self.ui.btn_run.setText(u"  开始抢菜")
        self.ui.btn_run.setIcon(QIcon(u":/assets/assets/run.png"))
        self.ui.btn_run.setStyleSheet("""
                    QPushButton{
                        color: white;
                        background-color: #5cb85c;
                        border: 1px solid #54ad5a;
                        border-radius: 4px;
                        padding: 2px;
                    }

                    QPushButton::hover{
                        background-color: #4cae4c;
                        border: 1px solid #449d44;
                    }
        """)

    def on_thread_start(self):
        self.is_running = True
        self.append_log("开始执行抢菜程序.....")
        self.ui.is_dingdong.setEnabled(False)
        self.ui.is_meituan.setEnabled(False)
        self.ui.btn_run.setText(u"  停止抢菜")
        self.ui.btn_run.setIcon(QIcon(u":/assets/assets/delete.png"))
        self.ui.btn_run.setStyleSheet("""
            QPushButton{
                color: white;
                background-color: #d9534f;
                border: 1px solid #d43f3a;
                border-radius: 4px;
                padding: 2px;
            }
            
            QPushButton::hover{
                background-color: #c9302c;
                border: 1px solid #ac2925;
            }
        """)

    @Slot(dict)
    def on_progress(self, progress: dict):
        msg = progress["msg"]
        msg_type = progress.get("type", 1)
        self.append_log(msg, msg_type)

    def append_log(self, msg: str, msg_type: int = 0):
        curr_time = datetime.now()
        time_str = datetime.strftime(curr_time, '%Y-%m-%d %H:%M:%S')
        color = COLORS[msg_type]
        log = f"<p style='color:{color}'>{time_str}  {msg}</p>"
        self.ui.textEdit.append(log)
