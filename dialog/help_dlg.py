# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'help_dlg.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFrame, QHBoxLayout, QLabel, QSizePolicy,
    QTextBrowser, QVBoxLayout, QWidget)
import resource_rc

class Ui_HelpDialog(object):
    def setupUi(self, HelpDialog):
        if not HelpDialog.objectName():
            HelpDialog.setObjectName(u"HelpDialog")
        HelpDialog.resize(519, 426)
        icon = QIcon()
        icon.addFile(u":/assets/assets/logo2.png", QSize(), QIcon.Normal, QIcon.Off)
        HelpDialog.setWindowIcon(icon)
        HelpDialog.setModal(True)
        self.verticalLayout_2 = QVBoxLayout(HelpDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_2 = QWidget(HelpDialog)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 80))
        self.widget_2.setMaximumSize(QSize(16777215, 80))
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(60, 60))
        self.label_4.setMaximumSize(QSize(60, 60))
        self.label_4.setPixmap(QPixmap(u":/assets/assets/logo2.png"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_4)

        self.widget = QWidget(self.widget_2)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(22, 51, 102);")

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(10)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: #666666;")
        self.label_2.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_2)


        self.horizontalLayout.addWidget(self.widget)


        self.verticalLayout_2.addWidget(self.widget_2)

        self.textBrowser = QTextBrowser(HelpDialog)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setFrameShape(QFrame.NoFrame)
        self.textBrowser.setFrameShadow(QFrame.Plain)

        self.verticalLayout_2.addWidget(self.textBrowser)

        self.buttonBox = QDialogButtonBox(HelpDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.retranslateUi(HelpDialog)
        self.buttonBox.accepted.connect(HelpDialog.accept)
        self.buttonBox.rejected.connect(HelpDialog.reject)

        QMetaObject.connectSlotsByName(HelpDialog)
    # setupUi

    def retranslateUi(self, HelpDialog):
        HelpDialog.setWindowTitle(QCoreApplication.translate("HelpDialog", u"\u5e2e\u52a9", None))
        self.label_4.setText("")
        self.label.setText(QCoreApplication.translate("HelpDialog", u"\u5305\u83dc\u672a\u80fd\u627e\u5230\u60a8\u7684\u8bbe\u5907", None))
        self.label_2.setText(QCoreApplication.translate("HelpDialog", u"\u4e0d\u8981\u6c14\u9981\uff0c\u627e\u4e0d\u5230\u8bbe\u5907\u5f88\u5e38\u89c1\u3002\u8bf7\u6839\u636e\u4e0b\u9762\u7684\u6307\u5f15\u68c0\u67e5\u60a8\u7684\u8bbe\u5907\u72b6\u6001", None))
        self.textBrowser.setHtml(QCoreApplication.translate("HelpDialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:9px; margin-bottom:0px; margin-left:9px; margin-right:9px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:9px; margin-bottom:0px; margin-left:9px; margin-right:9px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:700; color:#00007f;\">1. \u68c0\u67e5\u624b\u673a\u662f\u5426\u5f00\u542f\u4e86USB\u8c03\u8bd5</span>    </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:9px; margin-right:9px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u90e8\u5206Android\u624b\u673a\u4e0e\u7535\u8111\u901a\u4fe1"
                        "\u9700\u8981\u5f00\u542fUSB\u8c03\u8bd5\u6a21\u5f0f\u3002\u4e0d\u540c\u578b\u53f7\u624b\u673a\u5f00\u542fUSB\u8c03\u8bd5\u7684\u65b9\u6cd5\u4e0d\u540c\uff0c\u5177\u4f53\u8bf7\u53c2\u8003: </span><a href=\"https://zhuanlan.zhihu.com/p/429854110\"><span style=\" font-size:10pt; text-decoration: underline; color:#0000ff;\">\u534e\u4e3a\u624b\u673a\u5f00\u542fUSB\u8c03\u8bd5\uff0c </span></a><a href=\"https://www.bkqs.com.cn/content/zn2o02qpy.html\"><span style=\" font-size:10pt; text-decoration: underline; color:#0000ff;\">\u5c0f\u7c73\u624b\u673a\u5f00\u542fUSB\u8c03\u8bd5,</span></a><a href=\"https://zhuanlan.zhihu.com/p/429854110\"><span style=\" font-size:10pt; text-decoration: underline; color:#0000ff;\"> </span></a><a href=\"https://blog.csdn.net/weixin_31100713/article/details/117644271\"><span style=\" font-size:10pt; text-decoration: underline; color:#0000ff;\">OPPO\u624b\u673a\u5f00\u542fUSB\u8c03\u8bd5\uff0c </span></a><a href=\"https://www.jy135.com/shouji/162712.html\"><span style=\" font-size:10pt; "
                        "text-decoration: underline; color:#0000ff;\">vivo\u624b\u673a\u5f00\u542fUSB\u8c03\u8bd5\uff0c </span></a><a href=\"https://www.jy135.com/shouji/336013.html\"><span style=\" font-size:10pt; text-decoration: underline; color:#0000ff;\">\u4e09\u661f\u624b\u673a\u5f00\u542fUSB\u8c03\u8bd5</span></a>                \u3002    </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:9px; margin-right:9px; -qt-block-indent:0; text-indent:0px;\">    </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:9px; margin-right:9px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:700; color:#00007f;\">2. \u68c0\u67e5\u624b\u673a\u4e0e\u7535\u8111\u7684\u8fde\u63a5\u6a21\u5f0f\uff0c\u4e0d\u80fd\u662f\u201d\u4ec5\u5145\u7535\u201c</span>    </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:9px; margin-right:9px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#000000;\">\u5f00\u542fUSB\u8c03\u8bd5\u540e\u53ef\u80fd\u8fd8\u662f"
                        "\u627e\u4e0d\u5230\u8bbe\u5907\uff0c\u8fd9\u53ef\u80fd\u662f\u624b\u673a\u4e0e\u7535\u8111\u7684\u8fde\u63a5\u6a21\u5f0f\u4e0d\u5bf9\u3002\u4ee5\u534e\u4e3a\u624b\u673a\u4e3a\u4f8b\uff0c\u624b\u673a\u4e0e\u7535\u8111\u8fde\u63a5\u540e\u9ed8\u8ba4\u662f\u201d\u4ec5\u5145\u7535\u6a21\u5f0f\u201c\u3002\u6b64\u65f6\u9700\u8981\u4e0b\u6765\u5c55\u5f00\u7cfb\u7edf\u901a\u77e5\u83dc\u5355\uff0c\u70b9\u51fb\u201d\u6b63\u5728\u901a\u8fc7USB\u5145\u7535\u201c\uff0c\u5728\u5f39\u51fa\u7684USB\u8fde\u63a5\u65b9\u5f0f\u83dc\u5355\u4e2d\u9009\u62e9\u201dMIDI\u201c\u3002</span>        </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:9px; margin-right:9px; -qt-block-indent:0; text-indent:0px;\">    </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:9px; margin-right:9px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:700; color:#00007f;\">3. \u7ec8\u6781\u5927\u6cd5--Android\u6a21\u62df\u5668</span>    </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px"
                        "; margin-left:9px; margin-right:9px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#000000;\">\u5982\u679c\u4ee5\u4e0a\u65b9\u6cd5\u4ecd\u7136\u65e0\u6cd5\u594f\u6548\uff0c\u8bf7\u5c1d\u8bd5\u5728\u672c\u673a\u5b89\u88c5Android\u6a21\u62df\u5668\u3002\u63a8\u8350            </span><a href=\"https://mumu.163.com/mac/index.html \"><span style=\" text-decoration: underline; color:#0000ff;\">MUMU\u6a21\u62df\u5668 </span></a> \u6216 <a href=\"https://www.yeshen.com/\"><span style=\" text-decoration: underline; color:#0000ff;\">\u591c\u795e\u6a21\u62df\u5668</span></a></p></body></html>", None))
    # retranslateUi

