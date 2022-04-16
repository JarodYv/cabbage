import sys
from PySide6.QtWidgets import QApplication

import core.device
from MainWindow import MainWindow

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    core.device.play_voice("start")
    app = QApplication([])
    main_window = MainWindow()
    # main_window.setWindowFlags(Qt.CustomizeWindowHint)
    # main_window.showMaximized()
    main_window.show()
    sys.exit(app.exec())

