# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setting.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QHBoxLayout, QLabel, QSizePolicy,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)
import resource_rc

class Ui_SettingDialog(object):
    def setupUi(self, SettingDialog):
        if not SettingDialog.objectName():
            SettingDialog.setObjectName(u"SettingDialog")
        SettingDialog.resize(400, 300)
        icon = QIcon()
        icon.addFile(u":/assets/assets/logo2.png", QSize(), QIcon.Normal, QIcon.Off)
        SettingDialog.setWindowIcon(icon)
        SettingDialog.setModal(True)
        self.verticalLayout_2 = QVBoxLayout(SettingDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(SettingDialog)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(12, 12, 12, 12)
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(9, -1, 9, -1)
        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(100, 0))
        self.label_2.setMaximumSize(QSize(100, 16777215))
        font = QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.op_time = QSpinBox(self.widget_3)
        self.op_time.setObjectName(u"op_time")

        self.horizontalLayout_2.addWidget(self.op_time)


        self.verticalLayout.addWidget(self.widget_3)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(9, -1, 9, -1)
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(100, 0))
        self.label.setMaximumSize(QSize(100, 16777215))
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.err_time = QSpinBox(self.widget_2)
        self.err_time.setObjectName(u"err_time")
        self.err_time.setMinimum(1)
        self.err_time.setValue(5)

        self.horizontalLayout.addWidget(self.err_time)


        self.verticalLayout.addWidget(self.widget_2)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.play_sound = QCheckBox(self.widget_4)
        self.play_sound.setObjectName(u"play_sound")
        self.play_sound.setFont(font)
        self.play_sound.setChecked(True)

        self.horizontalLayout_3.addWidget(self.play_sound)


        self.verticalLayout.addWidget(self.widget_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.verticalLayout_2.addWidget(self.widget)

        self.buttonBox = QDialogButtonBox(SettingDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.retranslateUi(SettingDialog)
        self.buttonBox.accepted.connect(SettingDialog.accept)
        self.buttonBox.rejected.connect(SettingDialog.reject)

        QMetaObject.connectSlotsByName(SettingDialog)
    # setupUi

    def retranslateUi(self, SettingDialog):
        SettingDialog.setWindowTitle(QCoreApplication.translate("SettingDialog", u"\u8bbe\u7f6e", None))
        self.label_2.setText(QCoreApplication.translate("SettingDialog", u"\u62a2\u83dc\u64cd\u4f5c\u95f4\u9694(s): ", None))
        self.label.setText(QCoreApplication.translate("SettingDialog", u"\u5f02\u5e38\u91cd\u542f\u95f4\u9694(s): ", None))
        self.play_sound.setText(QCoreApplication.translate("SettingDialog", u"\u64ad\u653e\u58f0\u97f3", None))
    # retranslateUi

