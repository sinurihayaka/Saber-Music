import sys,os
import json as j
from MainWindow import *
from searchModel import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import About
import webbrowser
from PyQt5 import QtCore, QtGui, QtWidgets


class windowMain(QMainWindow):
    def __init__(self):
        super(windowMain, self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        #浏览器
        self.ui.browser = QWebEngineView(self.ui.centralwidget)
        self.ui.browser.setGeometry(QtCore.QRect(300, 722, 200, 95))
        # 加载外部的web界面
        self.ui.browser.load(QUrl(""))
        self.ui.browser.raise_()

        #隐藏窗口
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.show()
        #绑定按钮
        self.ui.AboutButton.clicked.connect(self.about)
        self.ui.pushButton.clicked.connect(self.search)
        self.ui.hide.clicked.connect(self.hideCommand)
        self.ui.browseButton.clicked.connect(self.browseCommand)
        self.ui.loveButton.clicked.connect(self.loveCommand)
        #下拉框
        itemlist=["酷狗音乐(推荐)","酷我音乐"]
        self.ui.comboBox.addItems(itemlist)
        #添加表头
        self.model = QStandardItemModel(self)
        self.model.setHorizontalHeaderLabels(['歌曲名', '歌手','歌曲地址'])
        self.ui.treeView.setModel(self.model)

        self.model2 = QStandardItemModel(self)
        self.model2.setHorizontalHeaderLabels(['歌曲名', '歌手', '歌曲地址'])
        self.ui.treeView_2.setModel(self.model2)
        #更改表头宽度(第x列，像素)
        self.ui.treeView.header().resizeSection(0, 300)
        self.ui.treeView.header().resizeSection(1, 200)

        self.ui.treeView_2.header().resizeSection(0, 300)
        self.ui.treeView_2.header().resizeSection(1, 200)
        #绑定treeview点击
        self.ui.treeView.clicked.connect(self.onCurrentChanged)

        self.ui.treeView_2.clicked.connect(self.onCurrentChanged2)
        #识别tab
        self.ui.tabWidget.currentChanged.connect(self.loadTab)
        self.tabNum = 1
        #加载喜欢的音乐
        try:
            with open("D:/SaberMusic喜爱的音乐.json", "r") as f:
                pass
        except Exception as e:
            if str(e) == "[Errno 2] No such file or directory: 'D:/SaberMusic喜爱的音乐.json'":
                with open("D:/SaberMusic喜爱的音乐.json", "w") as f:
                    pass
            else:
                print(e)
        else:
            self.loadLove()


        """
                        最小化右键菜单
                        :return:
                        """
        # 初始化菜单单项
        self.quitAppAction = QtWidgets.QAction("退出")

        # 菜单单项连接方法
        self.quitAppAction.triggered.connect(self.quitApp)

        # 初始化菜单列表
        self.trayIconMenu = QtWidgets.QMenu()
        self.trayIconMenu.addSeparator()
        self.trayIconMenu.addAction(self.quitAppAction)

        # 构建菜单UI
        self.trayIcon = QtWidgets.QSystemTrayIcon()
        self.trayIcon.setContextMenu(self.trayIconMenu)
        self.trayIcon.setIcon(QtGui.QIcon("./res/pics/saber.ico"))
        self.trayIcon.setToolTip("Saber Music")
        # 左键双击打开主界面
        self.trayIcon.activated[QtWidgets.QSystemTrayIcon.ActivationReason].connect(self.openMainWindow)
        # 允许托盘菜单显示
        self.trayIcon.show()

    def hideCommand(self):
        try:
            self.ui.centralwidget.setWindowFlags(QtCore.Qt.ToolTip)
            self.ui.centralwidget.hide()
        except Exception as e:
            print(e)

    #获取tab
    def loadTab(self,x):
        if x == 0:
            self.tabNum = 1
        else:
            self.tabNum = 2

        #获取treeview当前行数及ID

    def loadLove(self):
        # 清空treeView(重置model)
        self.model2 = QStandardItemModel(self)
        self.model2.setHorizontalHeaderLabels(['歌曲名', '歌手', '歌曲地址'])
        self.ui.treeView_2.setModel(self.model2)
        with open("D:/SaberMusic喜爱的音乐.json", "r") as f:
            try:
                self.loveDict = j.load(f)
            except Exception as e:
                print(e)
            else:
                a = 0
                for i in self.loveDict:
                    try:
                        itemProject = QStandardItem(self.loveDict[i][0])
                        self.model2.appendRow(itemProject)
                        self.model2.setItem(a, 1, QStandardItem(self.loveDict[i][1]))
                        self.model2.setItem(a, 2, QStandardItem(i))
                    except Exception as e:
                        print(e)
                    else:
                        a += 1

    def onCurrentChanged(self,current):
        self.currentRow = current.row()  #行数
        #Id
        if current.column() == 2:
            self.currentId = str(current.data())
        else:
            self.currentId = str(current.sibling(current.row(), 2).data())
        self.ui.browser.load(QUrl(self.currentId))

        #曲名
        if current.column() == 0:
            self.currentName = str(current.data())
        else:
            self.currentName = str(current.sibling(current.row(), 0).data())

        # 歌手
        if current.column() == 1:
            self.currentSinger = str(current.data())
        else:
            self.currentSinger = str(current.sibling(current.row(), 1).data())

    def onCurrentChanged2(self,current):
        self.currentRow = current.row()  # 行数
        # Id
        if current.column() == 2:
            self.currentId2 = str(current.data())
        else:
            self.currentId2 = str(current.sibling(current.row(), 2).data())
        self.ui.browser.load(QUrl(self.currentId2))


    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton and self.isMaximized() == False:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, mouse_event):
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(mouse_event.globalPos() - self.m_Position)  # 更改窗口位置
            mouse_event.accept()

    def mouseReleaseEvent(self, mouse_event):
        self.m_flag = False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

    def search(self):
        if self.ui.lineEdit.text() == "":
            msg_box = QMessageBox(QMessageBox.Critical, 'Saber老婆的温馨提示', "请输入搜索关键词")
            msg_box.exec_()

        else:
            #清空treeView(重置model)
            self.model = QStandardItemModel(self)
            self.model.setHorizontalHeaderLabels(['歌曲名', '歌手', '歌曲地址'])
            self.ui.treeView.setModel(self.model)

            #获取下拉框(音乐软件)
            self.mode = self.ui.comboBox.currentText()

            self.ui.textEdit.append(self.mode+"搜索："+self.ui.lineEdit.text())

            #调用搜索
            if self.mode == "酷我音乐":
                self.searchThread=kuwosearchThread(self.ui.lineEdit.text(),self.model)
                self.searchThread.start()
            elif self.mode == "酷狗音乐(推荐)":
                self.searchThread=kugousearchThread(self.ui.lineEdit.text(),self.model)
                self.searchThread.start()

    def browseCommand(self):
        try:
            str(self.currentId)
        except Exception as e:
            if str(e) == "'windowMain' object has no attribute 'currentId'":
                msg_box = QMessageBox(QMessageBox.Critical, 'Saber老婆的温馨提示', "请选择歌曲：）")
                msg_box.exec_()
            else:
                msg_box = QMessageBox(QMessageBox.Critical, '错误', str(e))
                msg_box.exec_()
        else:
            self.ui.textEdit.append(self.mode + "播放：" + self.currentId)
            webbrowser.open_new_tab(self.currentId)

    def loveCommand(self):
        if self.tabNum == 1:
            try:
                str(self.currentId)
            except Exception as e:
                print(e)
            else:
                with open("D:/SaberMusic喜爱的音乐.json", "r") as f:
                    try:
                        self.loveDict = j.load(f)
                    except Exception as e:
                         self.loveDict = {self.currentId:[self.currentName,self.currentSinger]}
                    else:
                        if self.currentId in self.loveDict:
                            del self.loveDict[self.currentId]
                        else:
                            self.loveDict.update({self.currentId:[self.currentName,self.currentSinger]})
                with open("D:/SaberMusic喜爱的音乐.json", "w") as f:
                    j.dump(self.loveDict,f)
                self.loadLove()

        elif self.tabNum == 2:
            try:
                str(self.currentId2)
            except Exception as e:
                print(e)
            else:
                with open("D:/SaberMusic喜爱的音乐.json", "r") as f:
                    self.loveDict = j.load(f)
                    del self.loveDict[self.currentId2]
                with open("D:/SaberMusic喜爱的音乐.json", "w") as f:
                    j.dump(self.loveDict, f)
                self.loadLove()

    def openMainWindow(self, reason):
        """
        双击打开主界面并使其活动
        :param reason:
        :return:
        """
        if reason == QtWidgets.QSystemTrayIcon.DoubleClick:
            self.ui.centralwidget.setWindowFlags(QtCore.Qt.Widget)
            self.ui.centralwidget.showNormal()
            self.ui.centralwidget.activateWindow()

    def quitApp(self):
        """
        包含二次确认的退出
        :return:
        """
        checkFlag = QtWidgets.QMessageBox.information(self.ui.centralwidget, "退出确认", "是否确认退出？",
                                                      QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if checkFlag == QtWidgets.QMessageBox.Yes:
            self.trayIcon.setVisible(False)
            QtWidgets.qApp.quit()
        else:
            pass



    def about(self):
        self.aboutwindow=windowAbout()
        
class windowAbout(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = About.Ui_Form()
        self.ui.setupUi(self)
        self.show()

        self.ui.biliButton.clicked.connect(self.openbili)
        self.ui.githubButton.clicked.connect(self.opengithub)

    def openbili(self):
        webbrowser.open_new_tab("https://space.bilibili.com/597860086")

    def opengithub(self):
        webbrowser.open_new_tab("https://github.com/sinurihayaka")


    #资源文件目录访问
def source_path(relative_path):
    #是否BundLe Resource
    if getattr(sys,'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path,relative_path)


if __name__ == "__main__":
    cd = source_path('')
    os.chdir(cd)
    app = QApplication(sys.argv)
    mainwindow=windowMain()
    sys.exit(app.exec_())
