# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wallpaper_loop.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import res


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1058, 867)
        # 隐藏非边框
        Form.setWindowFlags(Qt.FramelessWindowHint)
        # 背景透明
        Form.setAttribute(Qt.WA_TranslucentBackground)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 120, 394, 600))
        self.label.setStyleSheet(u"background-image: url(:/img/img/147.png);\n"
                                 "border-top-left-radius: 40;\n"
                                 "border-bottom-left-radius: 40;")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(360, 120, 661, 600))
        self.label_2.setStyleSheet(u"background-color: #161A20;\n"
                                   "border-top-right-radius: 40;\n"
                                   "border-bottom-right-radius: 40;")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(600, 140, 141, 41))
        font = QFont()
        font.setFamily(u"\u96b6\u4e66")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: white;")
        self.listWidget = QListWidget(Form)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(380, 320, 621, 381))
        self.listWidget.setStyleSheet(u"background-color: #161A20;\n"
                                      "color:white;")
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(380, 240, 531, 31))
        self.lineEdit.setStyleSheet(u"color: white;\n"
                                    "background-color: #161A20;")
        self.pushButton_mini = QPushButton(Form)
        self.pushButton_mini.setObjectName(u"pushButton_mini")
        self.pushButton_mini.setGeometry(QRect(950, 140, 20, 20))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setWeight(50)
        self.pushButton_mini.setFont(font1)
        self.pushButton_mini.setStyleSheet(u"QPushButton{\n"
                                           "background-color: rgb(188, 255, 116);\n"
                                           "border-radius:10px; \n"
                                           "color:black;}\n"
                                           "QPushButton:hover{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(189, 202, 250, 255), stop:1 rgba(255, 255, 255, 255))\n"
                                           "}\n"
                                           "QPushButton:pressed{padding-top:7px;\n"
                                           "padding-left:7px;}")
        self.pushButton_quit = QPushButton(Form)
        self.pushButton_quit.setObjectName(u"pushButton_quit")
        self.pushButton_quit.setGeometry(QRect(980, 140, 20, 20))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_quit.sizePolicy().hasHeightForWidth())
        self.pushButton_quit.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamily(u"AIGDT")
        font2.setPointSize(9)
        self.pushButton_quit.setFont(font2)
        self.pushButton_quit.setStyleSheet(u"QPushButton{\n"
                                           "background-color: red;\n"
                                           "border-radius:10px; \n"
                                           "color:black;}\n"
                                           "QPushButton:hover{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(189, 202, 250, 255), stop:1 rgba(255, 255, 255, 255))\n"
                                           "}\n"
                                           "QPushButton:pressed{padding-top:7px;\n"
                                           "padding-left:7px;}")
        self.pushButton_appendimg = QPushButton(Form)
        self.pushButton_appendimg.setObjectName(u"pushButton_appendimg")
        self.pushButton_appendimg.setGeometry(QRect(920, 240, 81, 28))
        self.pushButton_appendimg.setStyleSheet(u"QPushButton{\n"
                                                "background-color: white;\n"
                                                "border-radius:13px; \n"
                                                "color:black;}\n"
                                                "QPushButton:hover{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(189, 202, 250, 255), stop:1 rgba(255, 255, 255, 255))\n"
                                                "}\n"
                                                "QPushButton:pressed{padding-top:7px;\n"
                                                "padding-left:7px;}")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(770, 200, 91, 21))
        self.label_4.setStyleSheet(u"color: white;")
        self.spinBox = QSpinBox(Form)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(865, 200, 46, 22))
        self.spinBox.setStyleSheet(u"background-color: white;")
        self.spinBox.setValue(2)
        self.pushButton_start = QPushButton(Form)
        self.pushButton_start.setObjectName(u"pushButton_start")
        self.pushButton_start.setGeometry(QRect(920, 200, 81, 28))
        self.pushButton_start.setStyleSheet(u"QPushButton{\n"
                                            "background-color: white;\n"
                                            "border-radius:13px; \n"
                                            "color:black;}\n"
                                            "QPushButton:hover{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(189, 202, 250, 255), stop:1 rgba(255, 255, 255, 255))\n"
                                            "}\n"
                                            "QPushButton:pressed{padding-top:7px;\n"
                                            "padding-left:7px;}")
        self.checkBox = QCheckBox(Form)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(380, 200, 91, 19))
        self.checkBox.setStyleSheet(u"color:white;")
        self.checkBox.setChecked(True)
        self.label_info = QLabel(Form)
        self.label_info.setObjectName(u"label_info")
        self.label_info.setGeometry(QRect(380, 290, 531, 21))
        self.label_info.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_removeimg = QPushButton(Form)
        self.pushButton_removeimg.setObjectName(u"pushButton_removeimg")
        self.pushButton_removeimg.setGeometry(QRect(920, 280, 81, 28))
        self.pushButton_removeimg.setStyleSheet(u"QPushButton{\n"
                                                "background-color: white;\n"
                                                "border-radius:13px; \n"
                                                "color:black;}\n"
                                                "QPushButton:hover{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(189, 202, 250, 255), stop:1 rgba(255, 255, 255, 255))\n"
                                                "}\n"
                                                "QPushButton:pressed{padding-top:7px;\n"
                                                "padding-left:7px;}")
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(140, 670, 101, 41))
        font3 = QFont()
        font3.setFamily(u"\u534e\u6587\u4eff\u5b8b")
        self.label_5.setFont(font3)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"\u58c1\u7eb8\u8f6e\u64ad", None))
        self.pushButton_mini.setText("")
        self.pushButton_quit.setText("")
        self.pushButton_appendimg.setText(QCoreApplication.translate("Form", u"\u6dfb\u52a0\u56fe\u7247", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u8f6e\u64ad\u95f4\u9694(\u79d2)", None))
        self.pushButton_start.setText(QCoreApplication.translate("Form", u"\u542f\u52a8\u8f6e\u64ad", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"\u4fdd\u5b58\u8bbe\u7f6e", None))
        self.label_info.setText("")
        self.pushButton_removeimg.setText(QCoreApplication.translate("Form", u"\u5220\u9664\u56fe\u7247", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u51fa\u54c1: \u5f13\u592b\u6563\u4eba", None))
    # retranslateUi
