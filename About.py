# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'About.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(380, 530)
        Form.setMinimumSize(QtCore.QSize(380, 530))
        Form.setMaximumSize(QtCore.QSize(380, 530))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res/pics/saber.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 721, 481))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.gridLayoutWidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(100, 10, 251, 81))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 80, 80))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("res/pics/saber.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.biliButton = QtWidgets.QPushButton(self.frame)
        self.biliButton.setGeometry(QtCore.QRect(60, 110, 70, 70))
        self.biliButton.setStyleSheet("#biliButton\n"
"{\n"
"border:none;\n"
"}\n"
"#biliButton:hover\n"
"{\n"
"border:2px solid rgb(147, 147, 147);\n"
"border-radius:5px;\n"
"}")
        self.biliButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("res/pics/bilibili.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.biliButton.setIcon(icon1)
        self.biliButton.setIconSize(QtCore.QSize(70, 70))
        self.biliButton.setObjectName("biliButton")
        self.githubButton = QtWidgets.QPushButton(self.frame)
        self.githubButton.setGeometry(QtCore.QRect(200, 110, 70, 70))
        self.githubButton.setStyleSheet("#githubButton\n"
"{\n"
"border:none;\n"
"}\n"
"#githubButton:hover\n"
"{\n"
"border:2px solid rgb(147, 147, 147);\n"
"border-radius:5px;\n"
"}")
        self.githubButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("res/pics/github.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.githubButton.setIcon(icon2)
        self.githubButton.setIconSize(QtCore.QSize(57, 57))
        self.githubButton.setObjectName("githubButton")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(100, 40, 251, 81))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 210, 343, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.line = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(10, 310, 151, 111))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("res/pics/saberx.jpg"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(162, 290, 3, 150))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(190, 310, 121, 121))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("res/pics/saber.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "关于"))
        self.label.setText(_translate("Form", "作者：SinuriHayaka"))
        self.label_3.setText(_translate("Form", "版本：v0.3.1-alpha"))
        self.label_4.setText(_translate("Form", "背景图片：昇空\n"
"PixivId:47987765"))
        self.label_5.setText(_translate("Form", "图标：好喝不过矿泉水\n"
"PixivId:60551841"))
