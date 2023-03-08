import sys,os
from MainWindow import *
from PyQt5.QtWidgets import *
from PyQt5.Qt import QThread
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from searchModel import *
from playModel import *
import About
import webbrowser


class windowMain(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        #隐藏窗口
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.show()
        #绑定按钮
        self.ui.AboutButton.clicked.connect(self.about)
        self.ui.pushButton.clicked.connect(self.search)
        self.ui.pushButton_4.clicked.connect(self.play)
        #下拉框
        itemlist=["酷我音乐(推荐)","酷狗音乐"]
        self.ui.comboBox.addItems(itemlist)
        #添加表头
        self.model = QStandardItemModel(self)
        self.model.setHorizontalHeaderLabels(['歌曲名', '歌手','歌曲id'])
        self.ui.treeView.setModel(self.model)
        #更改表头宽度(第x列，像素)
        self.ui.treeView.header().resizeSection(0, 300)
        self.ui.treeView.header().resizeSection(1, 200)
        #绑定treeview点击
        self.ui.treeView.clicked.connect(self.onCurrentChanged)

        #获取treeview当前行数及ID
    def onCurrentChanged(self,current):
        self.currentRow = current.row()  #行数
        #Id
        if current.column() == 2:
            self.currentId = str(current.data())
        else:
            self.currentId = str(current.sibling(current.row(), 2).data())


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
        #清空treeView(重置model)
        self.model = QStandardItemModel(self)
        self.model.setHorizontalHeaderLabels(['歌曲名', '歌手', '歌曲id'])
        self.ui.treeView.setModel(self.model)

        #获取下拉框(音乐软件)
        self.mode = self.ui.comboBox.currentText()

        self.ui.textEdit.append(self.mode+"搜索："+self.ui.lineEdit.text())

        #调用搜索
        if self.mode == "酷我音乐(推荐)":
            self.searchThread=kuwosearchThread(self.ui.lineEdit.text(),self.model)
            self.searchThread.start()
        elif self.mode == "酷狗音乐":
            self.searchThread=kugousearchThread(self.ui.lineEdit.text(),self.model)
            self.searchThread.start()

    #播放音乐
    def play(self):
        try:
            self.playThread = playThread(self.mode,self.currentId,self.ui.textEdit)
        except Exception as e:
            if repr(e) == """AttributeError("'windowMain' object has no attribute 'mode'")""":
                msg_box = QMessageBox(QMessageBox.Critical, 'Saber老婆的温馨提示', "请选择要播放的音乐")
                msg_box.exec_()
            else:
                msg_box = QMessageBox(QMessageBox.Critical, '错误', repr(e))
                msg_box.exec_()
        else:
            self.playThread.start()

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
