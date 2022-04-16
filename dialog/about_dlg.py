# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about_dlg.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import resource_rc

class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        if not AboutDialog.objectName():
            AboutDialog.setObjectName(u"AboutDialog")
        AboutDialog.resize(400, 300)
        icon = QIcon()
        icon.addFile(u":/assets/assets/logo2.png", QSize(), QIcon.Normal, QIcon.Off)
        AboutDialog.setWindowIcon(icon)
        AboutDialog.setModal(True)
        self.verticalLayout = QVBoxLayout(AboutDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_2 = QWidget(AboutDialog)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 9, 0, 0)
        self.horizontalSpacer = QSpacerItem(98, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(64, 64))
        self.label.setMaximumSize(QSize(64, 64))
        self.label.setPixmap(QPixmap(u":/assets/assets/logo2.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(98, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.widget_2)

        self.label_4 = QLabel(AboutDialog)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color: rgb(22, 51, 102);")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_4)

        self.label_3 = QLabel(AboutDialog)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(10)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: #BBBBBB;")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)

        self.label_5 = QLabel(AboutDialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"margin: 0px 20px;\n"
"color: #bbbbbb;")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_5.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_5)

        self.label_6 = QLabel(AboutDialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"color:#bbbbbb;")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_6.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_6)

        self.verticalSpacer = QSpacerItem(20, 107, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label_2 = QLabel(AboutDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: #BBBBBB;")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)


        self.retranslateUi(AboutDialog)

        QMetaObject.connectSlotsByName(AboutDialog)
    # setupUi

    def retranslateUi(self, AboutDialog):
        AboutDialog.setWindowTitle(QCoreApplication.translate("AboutDialog", u"\u5173\u4e8e", None))
        self.label.setText("")
        self.label_4.setText(QCoreApplication.translate("AboutDialog", u"\u5305\u83dc", None))
        self.label_3.setText(QCoreApplication.translate("AboutDialog", u"version: 1.0.0", None))
        self.label_5.setText(QCoreApplication.translate("AboutDialog", u"\u5305\u83dc\u662f\u8c31\u84dd\u4e3a\u4e0a\u6d77\u4eba\u6c11\u5f00\u53d1\u7684\u4e00\u6b3e\u81ea\u52a8\u62a2\u83dc\u8f6f\u4ef6\uff0c\n"
"\u89e3\u51b3\u75ab\u60c5\u671f\u95f4\u4e0a\u6d77\u4eba\u6c11\u5403\u83dc\u96be\u7684\u95ee\u9898\u3002", None))
        self.label_6.setText(QCoreApplication.translate("AboutDialog", u"\u5305\u83dc\u62e5\u6709\u53cb\u597d\u7684\u7528\u6237\u754c\u9762\uff0c\u4e0d\u9700\u8981\u590d\u6742\u914d\u7f6e\uff0c\n"
"\u4e0d\u9700\u8981\u6293\u5305\u83b7\u53d6token\uff0c\u5f00\u7bb1\u5373\u7528\uff0c\u5c0f\u767d\u4e5f\u80fd\u5feb\u901f\u4e0a\u624b\u4f7f\u7528\u3002", None))
        self.label_2.setText(QCoreApplication.translate("AboutDialog", u"Copyright \u00a9 2022 PlanPlus Inc. All Rights Reserved", None))
    # retranslateUi

