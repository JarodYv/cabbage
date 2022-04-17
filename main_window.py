# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHBoxLayout,
    QLabel, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(790, 600)
        icon = QIcon()
        icon.addFile(u":/assets/assets/logo2.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QWidget(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setMinimumSize(QSize(0, 60))
        self.header.setMaximumSize(QSize(16777215, 60))
        self.header.setStyleSheet(u"QWidget#header{\n"
"	background-color: rgb(71, 120, 199);\n"
"	background-image:url(:/assets/assets/menu_bg.png);\n"
"	background-image:url(:/assets/assets/menu_bg.png);\n"
"	background-repeat:no-repeat;\n"
"	background-position:bottom;\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.header)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(12, 0, 0, 0)
        self.label = QLabel(self.header)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(60, 36))
        self.label.setMaximumSize(QSize(60, 36))
        self.label.setStyleSheet(u"margin: 0 12px;")
        self.label.setPixmap(QPixmap(u":/assets/assets/logo.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.header)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.header)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(11)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: white;")

        self.horizontalLayout.addWidget(self.label_3)

        self.horizontalSpacer = QSpacerItem(373, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_home = QPushButton(self.header)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(60, 60))
        self.btn_home.setMaximumSize(QSize(60, 60))
        self.btn_home.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(255, 255, 255, 26);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/assets/assets/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_home.setIcon(icon1)
        self.btn_home.setIconSize(QSize(20, 20))
        self.btn_home.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_home)

        self.btn_setting = QPushButton(self.header)
        self.btn_setting.setObjectName(u"btn_setting")
        self.btn_setting.setMinimumSize(QSize(60, 60))
        self.btn_setting.setMaximumSize(QSize(60, 60))
        self.btn_setting.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(255, 255, 255, 26);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/assets/assets/setting.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_setting.setIcon(icon2)
        self.btn_setting.setIconSize(QSize(20, 20))
        self.btn_setting.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_setting)

        self.btn_about = QPushButton(self.header)
        self.btn_about.setObjectName(u"btn_about")
        self.btn_about.setMinimumSize(QSize(60, 60))
        self.btn_about.setMaximumSize(QSize(60, 60))
        self.btn_about.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(255, 255, 255, 26);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/assets/assets/info.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_about.setIcon(icon3)
        self.btn_about.setIconSize(QSize(20, 20))
        self.btn_about.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_about)


        self.verticalLayout.addWidget(self.header)

        self.body = QWidget(self.centralwidget)
        self.body.setObjectName(u"body")
        self.body.setStyleSheet(u"background-color: rgb(243, 248, 254);")
        self.verticalLayout_2 = QVBoxLayout(self.body)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.stackedWidget = QStackedWidget(self.body)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.verticalLayout_6 = QVBoxLayout(self.page_1)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.widget_2 = QWidget(self.page_1)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(80, 80))
        self.label_4.setMaximumSize(QSize(80, 80))
        self.label_4.setPixmap(QPixmap(u":/assets/assets/logo2.png"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.widget = QWidget(self.widget_2)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        font2 = QFont()
        font2.setPointSize(16)
        font2.setBold(True)
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"color: rgb(22, 51, 102);")

        self.verticalLayout_3.addWidget(self.label_5)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        font3 = QFont()
        font3.setPointSize(10)
        self.label_6.setFont(font3)
        self.label_6.setStyleSheet(u"color: #666666;")
        self.label_6.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.label_6)

        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font3)
        self.label_7.setStyleSheet(u"color: #666666;")
        self.label_7.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.label_7)


        self.horizontalLayout_2.addWidget(self.widget)


        self.verticalLayout_6.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.page_1)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_5 = QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_8 = QLabel(self.widget_3)
        self.label_8.setObjectName(u"label_8")
        font4 = QFont()
        font4.setPointSize(11)
        font4.setBold(True)
        self.label_8.setFont(font4)
        self.label_8.setStyleSheet(u"color: rgb(22, 51, 102);")

        self.verticalLayout_5.addWidget(self.label_8)

        self.widget_4 = QWidget(self.widget_3)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setStyleSheet(u"QWidget{\n"
"color: #666666;\n"
"}\n"
"\n"
"")
        self.verticalLayout_4 = QVBoxLayout(self.widget_4)
        self.verticalLayout_4.setSpacing(12)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget_7 = QWidget(self.widget_4)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.widget_7)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(70, 0))
        self.label_15.setMaximumSize(QSize(70, 16777215))
        self.label_15.setFont(font3)
        self.label_15.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_15)

        self.label_9 = QLabel(self.widget_7)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font3)
        self.label_9.setWordWrap(True)

        self.horizontalLayout_5.addWidget(self.label_9)


        self.verticalLayout_4.addWidget(self.widget_7)

        self.widget_8 = QWidget(self.widget_4)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.widget_8)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(70, 0))
        self.label_16.setMaximumSize(QSize(70, 16777215))
        self.label_16.setFont(font3)
        self.label_16.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_16)

        self.label_10 = QLabel(self.widget_8)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font3)
        self.label_10.setWordWrap(True)

        self.horizontalLayout_6.addWidget(self.label_10)


        self.verticalLayout_4.addWidget(self.widget_8)

        self.widget_9 = QWidget(self.widget_4)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.widget_9)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(70, 0))
        self.label_17.setMaximumSize(QSize(70, 16777215))
        self.label_17.setFont(font3)
        self.label_17.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

        self.horizontalLayout_7.addWidget(self.label_17)

        self.label_12 = QLabel(self.widget_9)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font3)
        self.label_12.setWordWrap(True)

        self.horizontalLayout_7.addWidget(self.label_12)


        self.verticalLayout_4.addWidget(self.widget_9)

        self.widget_10 = QWidget(self.widget_4)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.widget_10)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(70, 0))
        self.label_18.setMaximumSize(QSize(70, 16777215))
        self.label_18.setFont(font3)
        self.label_18.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_18)

        self.label_13 = QLabel(self.widget_10)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font3)
        self.label_13.setWordWrap(True)

        self.horizontalLayout_8.addWidget(self.label_13)


        self.verticalLayout_4.addWidget(self.widget_10)

        self.btn_tutor = QPushButton(self.widget_4)
        self.btn_tutor.setObjectName(u"btn_tutor")
        self.btn_tutor.setStyleSheet(u"QPushButton{\n"
"	color: #333;\n"
"	border: 1px solid #ccc;\n"
"	border-radius: 4px;\n"
"	margin: 0 20px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	border: 1px solid #adadad;\n"
"	background-color: #e6e6e6;\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_tutor)


        self.verticalLayout_5.addWidget(self.widget_4)

        self.verticalSpacer = QSpacerItem(20, 37, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.widget_6 = QWidget(self.widget_3)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_4 = QSpacerItem(334, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.label_14 = QLabel(self.widget_6)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(32, 32))
        self.label_14.setMaximumSize(QSize(32, 32))
        self.label_14.setPixmap(QPixmap(u":/assets/assets/logo2.png"))
        self.label_14.setScaledContents(True)
        self.label_14.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_14)

        self.horizontalSpacer_5 = QSpacerItem(334, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)


        self.verticalLayout_5.addWidget(self.widget_6)

        self.label_11 = QLabel(self.widget_3)
        self.label_11.setObjectName(u"label_11")
        font5 = QFont()
        font5.setPointSize(12)
        self.label_11.setFont(font5)
        self.label_11.setStyleSheet(u"color: rgb(22, 51, 102);")
        self.label_11.setLineWidth(1)
        self.label_11.setMidLineWidth(0)
        self.label_11.setAlignment(Qt.AlignCenter)
        self.label_11.setIndent(-1)

        self.verticalLayout_5.addWidget(self.label_11)

        self.widget_5 = QWidget(self.widget_3)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(270, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.btn_init = QPushButton(self.widget_5)
        self.btn_init.setObjectName(u"btn_init")
        self.btn_init.setMinimumSize(QSize(160, 50))
        self.btn_init.setMaximumSize(QSize(150, 50))
        self.btn_init.setFont(font1)
        self.btn_init.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	background-color: #337ab7;\n"
"	border: 1px solid #2e6da4;\n"
"	border-radius: 4px;\n"
"	padding-left: 16px;\n"
"	padding-right: 16px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: #286090;\n"
"	border: 1px solid #204d74;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/assets/assets/edge_view.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_init.setIcon(icon4)
        self.btn_init.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.btn_init)

        self.horizontalSpacer_3 = QSpacerItem(270, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout_5.addWidget(self.widget_5)


        self.verticalLayout_6.addWidget(self.widget_3)

        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_7 = QVBoxLayout(self.page_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, 0, -1, 0)
        self.widget_11 = QWidget(self.page_2)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setMinimumSize(QSize(0, 80))
        self.widget_11.setMaximumSize(QSize(16777215, 80))
        self.widget_11.setStyleSheet(u"QWidget{\n"
"	color: #0f5132;\n"
"    background-color: #d1e7dd;\n"
"	border: 1px solid #badbcc;\n"
"    border-radius: 5px;\n"
"}")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(16, -1, 16, -1)
        self.label_20 = QLabel(self.widget_11)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(60, 60))
        self.label_20.setMaximumSize(QSize(60, 60))
        self.label_20.setStyleSheet(u"border: none;")
        self.label_20.setPixmap(QPixmap(u":/assets/assets/logo2.png"))
        self.label_20.setScaledContents(True)

        self.horizontalLayout_9.addWidget(self.label_20)

        self.label_19 = QLabel(self.widget_11)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font3)
        self.label_19.setStyleSheet(u"border: none;")
        self.label_19.setWordWrap(True)

        self.horizontalLayout_9.addWidget(self.label_19)


        self.verticalLayout_7.addWidget(self.widget_11)

        self.device_list = QWidget(self.page_2)
        self.device_list.setObjectName(u"device_list")
        self.device_list.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	background-color: #5cb85c;\n"
"	border: 1px solid #5cb85c;\n"
"	border-radius: 4px;\n"
"	padding: 0 10px;\n"
"	margin: 0 40px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: #4cae4c;\n"
"	border: 1px solid #449d44;\n"
"}")
        self.verticalLayout_8 = QVBoxLayout(self.device_list)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.listWidget = QListWidget(self.device_list)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setStyleSheet(u"QListView::item{\n"
"	height:180px;\n"
"	border: none;\n"
"	outline: 0;\n"
"}\n"
"\n"
"QListView::item:focus{\n"
"	border:none;\n"
"}")
        self.listWidget.setFrameShape(QFrame.NoFrame)
        self.listWidget.setFrameShadow(QFrame.Plain)
        self.listWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listWidget.setProperty("showDropIndicator", False)
        self.listWidget.setSelectionMode(QAbstractItemView.NoSelection)

        self.verticalLayout_8.addWidget(self.listWidget)


        self.verticalLayout_7.addWidget(self.device_list)

        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.body)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u5305\u83dc--\u5305\u4f60\u6709\u83dc", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u5305\u83dc", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"-- \u5305\u4f60\u6709\u83dc", None))
#if QT_CONFIG(tooltip)
        self.btn_home.setToolTip(QCoreApplication.translate("MainWindow", u"\u56de\u5230\u9996\u9875", None))
#endif // QT_CONFIG(tooltip)
        self.btn_home.setText("")
#if QT_CONFIG(tooltip)
        self.btn_setting.setToolTip(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
#endif // QT_CONFIG(tooltip)
        self.btn_setting.setText("")
#if QT_CONFIG(tooltip)
        self.btn_about.setToolTip(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
#endif // QT_CONFIG(tooltip)
        self.btn_about.setText("")
        self.label_4.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u6b22\u8fce\u4f7f\u7528\u5305\u83dc", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u5305\u83dc\u662f\u8c31\u84dd\u4e3a\u4e0a\u6d77\u4eba\u6c11\u5f00\u53d1\u7684\u4e00\u6b3e\u81ea\u52a8\u62a2\u83dc\u8f6f\u4ef6\uff0c\u89e3\u51b3\u75ab\u60c5\u671f\u95f4\u4e0a\u6d77\u4eba\u6c11\u5403\u83dc\u96be\u7684\u95ee\u9898\u3002", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u5305\u83dc\u62e5\u6709\u53cb\u597d\u7684\u7528\u6237\u754c\u9762\uff0c\u4e0d\u9700\u8981\u590d\u6742\u914d\u7f6e\uff0c\u4e0d\u9700\u8981\u6293\u5305\u83b7\u53d6token\uff0c\u5f00\u7bb1\u5373\u7528\uff0c\u5c0f\u767d\u4e5f\u80fd\u5feb\u901f\u4e0a\u624b\u4f7f\u7528\u3002", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u7b80\u6613\u6559\u7a0b", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u7b2c1\u6b65\uff1a", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u51c6\u59071\u90e8\u6216\u591a\u90e8Android\u624b\u673a\uff0c\u63d0\u524d\u5b89\u88c5\u767b\u5f55\u597d\u3010\u7f8e\u56e2\u5916\u5356\u3011\u6216\u3010\u53ee\u549a\u4e70\u83dc\u3011\uff1b", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u7b2c2\u6b65\uff1a", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u5c06\u624b\u673a\u4e0e\u7535\u8111\u8fde\u63a5\uff0c\u70b9\u51fb\u3010\u8bbe\u5907\u521d\u59cb\u5316\u3011\u6309\u94ae\uff0c\u5b8c\u6210\u8bbe\u5907\u68c0\u6d4b\u548c\u521d\u59cb\u5316\uff1b", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u7b2c3\u6b65\uff1a", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u5907\u521d\u59cb\u5316\u5b8c\u6210\u540e\uff0c\u8f6f\u4ef6\u4f1a\u8df3\u8f6c\u5230\u8bbe\u5907\u5217\u8868\u754c\u9762\u3002\u6253\u5f00\u3010\u7f8e\u56e2\u5916\u5356\u3011\u6216\u3010\u53ee\u549a\u4e70\u83dc\u3011\uff0c\u8fdb\u5165\u8d2d\u7269\u8f66\u754c\u9762\uff0c\n"
"\u786e\u8ba4\u8d2d\u7269\u8f66\u4e2d\u6709\u5546\u54c1\uff0c\u7136\u540e\u70b9\u51fb\u3010\u7f8e\u56e2\u62a2\u83dc\u3011\u6309\u94ae\u6216\u3010\u53ee\u549a\u62a2\u83dc\u3011\u6309\u94ae\uff1b", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u7b2c4\u6b65\uff1a", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u70b9\u51fb\u62a2\u83dc\u6309\u94ae\u540e\uff0c\u8f6f\u4ef6\u4f1a\u81ea\u52a8\u5237\u65b0\u754c\u9762\u5e2e\u4f60\u62a2\u83dc\uff0c\u62a2\u83dc\u5de5\u4f5c\u653e\u5fc3\u4ea4\u7ed9\u5305\u83dc\u5c31\u597d\u3002", None))
        self.btn_tutor.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u770b\u56fe\u6587\u7248\u6559\u7a0b", None))
        self.label_14.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u5305\u83dc\u5047\u8bbe\u60a8\u5df2\u7ecf\u51c6\u5907\u597d\u624b\u673a\uff0c\u63a5\u4e0b\u6765\u8fdb\u884c\u7b2c2\u6b65\u3010\u8bbe\u5907\u521d\u59cb\u5316\u3011\n"
"\u8bf7\u5c06Android\u624b\u673a\u8fde\u63a5\u672c\u7535\u8111\uff0c\u7136\u540e\u70b9\u51fb\u8bbe\u5907\u521d\u59cb\u5316\u6309\u94ae", None))
        self.btn_init.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u5907\u521d\u59cb\u5316", None))
        self.label_20.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u5305\u83dc\u652f\u6301\u591a\u53f0\u8bbe\u5907\u540c\u65f6\u8fd0\u884c\uff0c\u4f46\u4e00\u53f0\u8bbe\u5907\u540c\u4e00\u65f6\u95f4\u53ea\u80fd\u62a2\u4e00\u4e2a\u5e73\u53f0\u3002\n"
"\u8bf7\u6253\u5f00\u7f8e\u56e2\u5916\u5356\u6216\u53ee\u549a\u4e70\u83dc\uff0c\u8fdb\u5165\u8d2d\u7269\u8f66\u754c\u9762\uff0c\u7136\u540e\u70b9\u51fb\u4e0b\u65b9\u8bbe\u5907\u5217\u8868\u4e2d\u5bf9\u5e94\u5e73\u53f0\u7684\u62a2\u83dc\u6309\u94ae\u3002", None))
    # retranslateUi

