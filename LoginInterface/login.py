# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
        Form.resize(956, 795)

        # 隐藏非边框
        Form.setWindowFlags(Qt.FramelessWindowHint)
        # 背景透明
        Form.setAttribute(Qt.WA_TranslucentBackground)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 110, 371, 500))
        self.label.setStyleSheet(u"border-image: url(:/img/img/58.jpg);\n"
                                 "border-top-left-radius: 30px;\n"
                                 "border-bottom-left-radius: 30px")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(389, 110, 421, 500))
        self.label_2.setStyleSheet(u"border-top-right-radius: 30px;\n"
                                   "border: 1px solid violet;\n"
                                   "border-bottom-right-radius: 30px;\n"
                                   "background-color: rgb(255, 255, 255);")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(500, 160, 215, 50))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        font = QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"#pushButton{\n"
                                      "border:none;\n"
                                      "color:rgb(170, 0, 255);\n"
                                      "}\n"
                                      "#pushButton:focus {\n"
                                      "	color:gray;\n"
                                      "}\n"
                                      "")

        self.horizontalLayout.addWidget(self.pushButton)

        self.line = QFrame(self.widget)
        self.line.setObjectName(u"line")
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.line.setFont(font1)
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(u"#pushButton_2{\n"
                                        "border:none;\n"
                                        "color:rgb(170, 0, 255);\n"
                                        "}\n"
                                        "#pushButton_2:focus{\n"
                                        "	color: gray;\n"
                                        "}")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(430, 230, 351, 361))
        self.lineEdit = QLineEdit(self.widget_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(50, 70, 251, 51))
        self.lineEdit.setStyleSheet(u"border:1px solid rgb(170, 0, 255);\n"
                                    "border-radius:10px;")
        self.lineEdit_2 = QLineEdit(self.widget_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(50, 160, 251, 51))
        self.lineEdit_2.setStyleSheet(u"border:1px solid rgb(170, 0, 255);\n"
                                      "border-radius:10px;")
        self.pushButton_3 = QPushButton(self.widget_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(50, 260, 251, 41))
        font2 = QFont()
        font2.setPointSize(15)
        self.pushButton_3.setFont(font2)
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
                                        "background-color: rgb(170, 0, 255);\n"
                                        "border-radius:10px; \n"
                                        "color:rgb(0, 0, 0);}\n"
                                        "QPushButton:hover{background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 136, 252, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                        "}\n"
                                        "QPushButton:pressed{padding-top:7px;\n"
                                        "padding-left:7px;}")
        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(760, 120, 31, 28))
        font3 = QFont()
        font3.setFamily(u"Arial")
        self.pushButton_4.setFont(font3)
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
                                        "background-color: rgbA(0, 0, 0, 255);\n"
                                        "border-radius:10px; \n"
                                        "color:rgb(0, 0, 0);}\n"
                                        "QPushButton:hover{background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 136, 252, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                        "}\n"
                                        "QPushButton:pressed{padding-top:7px;\n"
                                        "padding-left:7px;}")
        self.pushButton_5 = QPushButton(Form)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(720, 120, 31, 28))
        font4 = QFont()
        font4.setFamily(u"Arial")
        font4.setPointSize(13)
        self.pushButton_5.setFont(font4)
        self.pushButton_5.setStyleSheet(u"QPushButton{\n"
                                        "background-color: rgbA(0, 0, 0, 255);\n"
                                        "border-radius:10px; \n"
                                        "color:rgb(0, 0, 0);}\n"
                                        "QPushButton:hover{background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 136, 252, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                        "}\n"
                                        "QPushButton:pressed{padding-top:7px;\n"
                                        "padding-left:7px;}")
        self.widget_3 = QWidget(Form)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(430, 190, 351, 351))
        self.lineEdit_5 = QLineEdit(self.widget_3)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(50, 60, 251, 51))
        self.lineEdit_5.setStyleSheet(u"border:1px solid rgb(170, 0, 255);\n"
                                      "border-radius:10px;")
        self.lineEdit_6 = QLineEdit(self.widget_3)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(50, 140, 251, 51))
        self.lineEdit_6.setStyleSheet(u"border:1px solid rgb(170, 0, 255);\n"
                                      "border-radius:10px;")
        self.lineEdit_7 = QLineEdit(self.widget_3)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(50, 220, 251, 51))
        self.lineEdit_7.setStyleSheet(u"border:1px solid rgb(170, 0, 255);\n"
                                      "border-radius:10px;")
        self.pushButton_7 = QPushButton(self.widget_3)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(50, 300, 251, 41))
        self.pushButton_7.setFont(font2)
        self.pushButton_7.setStyleSheet(u"QPushButton{\n"
                                        "background-color: rgb(170, 0, 255);\n"
                                        "border-radius:10px; \n"
                                        "color:rgb(0, 0, 0);}\n"
                                        "QPushButton:hover{background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 136, 252, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                        "}\n"
                                        "QPushButton:pressed{padding-top:7px;\n"
                                        "padding-left:7px;}")


        self.label_2.raise_()
        self.widget.raise_()
        self.widget_2.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.widget_3.raise_()
        self.label.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.label_2.setText("")
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u767b\u5f55", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u6ce8\u518c", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"\u8d26\u53f7:", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Form", u"\u5bc6\u7801:", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u767b  \u5f55", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"X", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"-", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("Form", u"\u8f93\u5165\u8d26\u53f7:", None))
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bbe\u7f6e\u5bc6\u7801:", None))
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("Form", u"\u786e\u8ba4\u5bc6\u7801:", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"\u6ce8  \u518c", None))
    # retranslateUi
