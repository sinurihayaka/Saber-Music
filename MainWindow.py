# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1300, 830)
        MainWindow.setMinimumSize(QtCore.QSize(1300, 830))
        MainWindow.setMaximumSize(QtCore.QSize(1300, 830))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res/pics/saber.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1301, 801))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("res/pics/background.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(170, 80, 281, 71))
        font = QtGui.QFont()
        font.setFamily("UD Digi Kyokasho NP-R")
        font.setPointSize(24)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(430, 80, 471, 71))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(24)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("#lineEdit\n"
"{\n"
"border-radius:20px;\n"
"background-color:#dedfa9;\n"
"color:white;\n"
"border-bottom:1px solid rgb(222,223,169);\n"
"}")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(910, 80, 51, 71))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton.setStyleSheet("#pushButton{\n"
"border: 1px solid #dcdfe6;\n"
"padding: 10px;\n"
"border-radius: 5px;}\n"
"\n"
"#pushButton:hover {\n"
"background-color: rgb(255,255,209);\n"
"border: 1px solid rgb(222,223,169);\n"
"}")
        self.pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("res/pics/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(45, 45))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(960, 160, 250, 561))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("#textEdit\n"
"{\n"
"border-radius:25px;\n"
"border:1px solid rgb(222,223,169);\n"
"background-color:#ffffdb;\n"
"}")
        self.textEdit.setDocumentTitle("")
        self.textEdit.setReadOnly(True)
        self.textEdit.setMarkdown("")
        self.textEdit.setObjectName("textEdit")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(90, 650, 201, 51))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(14)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("#comboBox{\n"
"border:1px solid rgb(188, 188, 188);\n"
"border-radius:10px;\n"
"}")
        self.comboBox.setEditable(False)
        self.comboBox.setCurrentText("")
        self.comboBox.setPlaceholderText("")
        self.comboBox.setObjectName("comboBox")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(870, 650, 71, 50))
        self.pushButton_4.setStyleSheet("#pushButton_4\n"
"{\n"
"border:none;\n"
"}\n"
"\n"
"#pushButton_4:hover{\n"
"padding-bottom:5px;\n"
"}\n"
"\n"
"#pushButton_4:pressed\n"
"{\n"
"padding-top:5px;\n"
"padding-left:5px;\n"
"}")
        self.pushButton_4.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("res/pics/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_4.setObjectName("pushButton_4")
        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(90, 160, 851, 481))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        self.treeView.setFont(font)
        self.treeView.setStyleSheet("#treeView\n"
"{\n"
"border-radius:20px;\n"
"border:1px solid rgb(222,223,169);\n"
"}")
        self.treeView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.treeView.setObjectName("treeView")
        self.AboutButton = QtWidgets.QPushButton(self.centralwidget)
        self.AboutButton.setGeometry(QtCore.QRect(90, 75, 75, 75))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AboutButton.sizePolicy().hasHeightForWidth())
        self.AboutButton.setSizePolicy(sizePolicy)
        self.AboutButton.setStyleSheet("#AboutButton{\n"
"border:none;\n"
"}\n"
"#AboutButton:hover {\n"
"border: 2px solid rgb(222,223,169);\n"
"border-radius:5px;\n"
"}")
        self.AboutButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("res/pics/saber.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AboutButton.setIcon(icon3)
        self.AboutButton.setIconSize(QtCore.QSize(70, 70))
        self.AboutButton.setObjectName("AboutButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(1040, 80, 61, 60))
        self.pushButton_3.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_3.setStyleSheet("#pushButton_3{\n"
"border: 1px solid #dcdfe6;\n"
"padding: 10px;\n"
"border-radius: 5px;}\n"
"\n"
"#pushButton_3:hover {\n"
"background-color: rgb(255,255,209);\n"
"border: 1px solid rgb(222,223,169);\n"
"}")
        self.pushButton_3.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("res/pics/hide.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon4)
        self.pushButton_3.setIconSize(QtCore.QSize(60, 60))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1120, 80, 60, 60))
        self.pushButton_2.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_2.setStyleSheet("#pushButton_2{\n"
"border: 1px solid #dcdfe6;\n"
"padding: 10px;\n"
"border-radius: 5px;}\n"
"\n"
"#pushButton_2:hover {\n"
"background-color: rgb(255,255,209);\n"
"border: 1px solid rgb(222,223,169);\n"
"}")
        self.pushButton_2.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("res/pics/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon5)
        self.pushButton_2.setIconSize(QtCore.QSize(60, 60))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.comboBox.setCurrentIndex(-1)
        self.pushButton_2.clicked.connect(MainWindow.close)
        self.pushButton_3.clicked.connect(MainWindow.showMinimized)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Saber Music"))
        self.label_3.setText(_translate("MainWindow", "Saber Music"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "搜索......"))
