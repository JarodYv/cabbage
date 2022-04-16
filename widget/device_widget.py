# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'device_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QRadioButton, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)
import resource_rc

class Ui_Device(object):
    def setupUi(self, Device):
        if not Device.objectName():
            Device.setObjectName(u"Device")
        Device.resize(737, 180)
        Device.setMinimumSize(QSize(0, 180))
        Device.setMaximumSize(QSize(16777215, 180))
        Device.setStyleSheet(u"QWidget:{\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(Device)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 9, 0, 9)
        self.widget_5 = QWidget(Device)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setStyleSheet(u"QWidget{\n"
"	color: #084298;\n"
"    background-color: #cfe2ff;\n"
"	border: 1px solid #b6d4fe;\n"
"    border-radius: 5px;\n"
"}")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.widget_5)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(280, 0))
        self.widget_4.setMaximumSize(QSize(280, 16777215))
        self.widget_4.setStyleSheet(u"QWidget{\n"
"	border-right: none;\n"
"	border-radius: 5px;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(self.widget_4)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color:none;\n"
"border: none;")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(40, 40))
        self.label.setMaximumSize(QSize(40, 40))
        self.label.setPixmap(QPixmap(u":/assets/assets/phone.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout = QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.device_name = QLabel(self.widget_2)
        self.device_name.setObjectName(u"device_name")
        font = QFont()
        font.setPointSize(11)
        self.device_name.setFont(font)

        self.verticalLayout.addWidget(self.device_name)

        self.device_id = QLabel(self.widget_2)
        self.device_id.setObjectName(u"device_id")
        self.device_id.setStyleSheet(u"color:#666666;")

        self.verticalLayout.addWidget(self.device_id)


        self.horizontalLayout.addWidget(self.widget_2)


        self.verticalLayout_2.addWidget(self.widget)

        self.widget_3 = QWidget(self.widget_4)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"background-color:none;\n"
"border: none;\n"
"margin: 0 12px;")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.is_dingdong = QRadioButton(self.widget_3)
        self.is_dingdong.setObjectName(u"is_dingdong")
        font1 = QFont()
        font1.setPointSize(10)
        self.is_dingdong.setFont(font1)
        icon = QIcon()
        icon.addFile(u":/assets/assets/dingdong.png", QSize(), QIcon.Normal, QIcon.Off)
        self.is_dingdong.setIcon(icon)
        self.is_dingdong.setIconSize(QSize(24, 24))
        self.is_dingdong.setChecked(True)

        self.horizontalLayout_2.addWidget(self.is_dingdong)

        self.is_meituan = QRadioButton(self.widget_3)
        self.is_meituan.setObjectName(u"is_meituan")
        self.is_meituan.setFont(font1)
        icon1 = QIcon()
        icon1.addFile(u":/assets/assets/meituan.png", QSize(), QIcon.Normal, QIcon.Off)
        self.is_meituan.setIcon(icon1)
        self.is_meituan.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.is_meituan)


        self.verticalLayout_2.addWidget(self.widget_3)

        self.btn_run = QPushButton(self.widget_4)
        self.btn_run.setObjectName(u"btn_run")
        self.btn_run.setMinimumSize(QSize(0, 32))
        self.btn_run.setMaximumSize(QSize(16777215, 32))
        self.btn_run.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	background-color: #5cb85c;\n"
"	border: 1px solid #5cb85c;\n"
"	border-radius: 4px;\n"
"	margin: 0 40px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: #4cae4c;\n"
"	border: 1px solid #449d44;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/assets/assets/run.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_run.setIcon(icon2)
        self.btn_run.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.btn_run)


        self.horizontalLayout_3.addWidget(self.widget_4)

        self.textEdit = QTextEdit(self.widget_5)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setStyleSheet(u"QTextEdit{\n"
"	background-color: white;\n"
"	border-left: none;\n"
"	border-top-left-radius: 0;\n"
"	border-bottom-left-radius: 0;\n"
"	padding: 6px;\n"
"}")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setFrameShadow(QFrame.Plain)
        self.textEdit.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.textEdit)


        self.verticalLayout_3.addWidget(self.widget_5)


        self.retranslateUi(Device)

        QMetaObject.connectSlotsByName(Device)
    # setupUi

    def retranslateUi(self, Device):
        Device.setWindowTitle(QCoreApplication.translate("Device", u"Form", None))
        self.label.setText("")
        self.device_name.setText(QCoreApplication.translate("Device", u"\u8bbe\u5907\u540d\u79f0", None))
        self.device_id.setText(QCoreApplication.translate("Device", u"\u8bbe\u5907id", None))
        self.is_dingdong.setText(QCoreApplication.translate("Device", u"\u53ee\u549a\u4e70\u83dc", None))
        self.is_meituan.setText(QCoreApplication.translate("Device", u"\u7f8e\u56e2\u5916\u5356", None))
        self.btn_run.setText(QCoreApplication.translate("Device", u"  \u5f00\u59cb\u62a2\u83dc", None))
        self.textEdit.setHtml(QCoreApplication.translate("Device", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
    # retranslateUi

