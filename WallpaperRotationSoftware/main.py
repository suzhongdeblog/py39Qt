import json
from threading import Thread
import win32api
import win32con
import win32gui
import os
import time
import sys
from PySide2.QtCore import Qt, QCoreApplication
from PySide2.QtGui import QCursor, QIcon
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog, QMenu, QAbstractItemView, QSystemTrayIcon, QAction
from wallpaper_loop import *

"""
# 使用auto-py-to-exe编译: 添加文件:图片文件夹,platforms,imageformats,PySide2.QtXml
"""
"""
# 隐藏非边框
Form.setWindowFlags(Qt.FramelessWindowHint)
# 背景透明
Form.setAttribute(Qt.WA_TranslucentBackground)
"""


class MyWindow(QMainWindow, Ui_Form):

    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.filelist, self.imgNo = self.init()
        self.play = 0
        # 链接到函数
        self.pushButton_start.clicked.connect(self.update)
        self.pushButton_appendimg.clicked.connect(self.setdir)
        self.pushButton_removeimg.clicked.connect(self.popitem)
        self.pushButton_quit.clicked.connect(self.quit)
        self.pushButton_mini.clicked.connect(self.mini)
        self.label_info.setText('等待启动轮播!')
        self.icon_quit()
        # 隐
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.SubWindow)

    # 保存设置
    def saveSetting(self):
        data = {'imgNo': self.imgNo, 'filelist': self.filelist}
        json_str = json.dumps(data,
                              ensure_ascii=False  # 针对中文必加
                              )
        with open('loopplay.ini', 'w', encoding='utf8') as f:
            f.write(json_str)

    # 删除列表项
    def popitem(self):
        self.label_info.setText('已删除图片: {}'.format(self.filelist[self.listWidget.currentRow()].split('\\')[-1]))
        self.listWidget.takeItem(self.listWidget.currentRow())  # 删除指定索引号的项目
        self.filelist.pop(self.listWidget.currentRow())

    # 提取设置进行初始化
    def init(self):
        if not os.path.exists('loopplay.ini'):
            self.filelist = []
            self.imgNo = 0
            return self.filelist, self.imgNo
        else:
            with open('loopplay.ini', 'r', encoding='utf8') as f:
                info = json.loads(f.read())
            self.filelist = info['filelist']
            self.imgNo = int(info['imgNo'])
            filenames = [i.split('\\')[-1] for i in self.filelist]
            for file in filenames:
                self.listWidget.addItem(file)
            return self.filelist, self.imgNo

    # 托盘化
    def icon_quit(self):
        mini_icon = QSystemTrayIcon(self)
        mini_icon.setIcon(QIcon('./img/夏米尔.png'))
        quit_menu = QAction('Exit', self, triggered=self.quit)
        show_menu = QAction('show', self, triggered=self.showNormal)
        tpMenu = QMenu(self)
        tpMenu.addAction(show_menu)
        tpMenu.addAction(quit_menu)
        mini_icon.setContextMenu(tpMenu)
        mini_icon.show()

    # 换墙纸的方法
    def Windows_img(self, paperPath):
        k = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control panel\\Desktop", 0, win32con.KEY_SET_VALUE)
        # 在注册表中写入属性值
        win32api.RegSetValueEx(k, "wapaperStyle", 0, win32con.REG_SZ, "2")  # 0 代表桌面居中 2 代表拉伸桌面
        win32api.RegSetValueEx(k, "Tilewallpaper", 0, win32con.REG_SZ, "0")
        win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, paperPath, win32con.SPIF_SENDWININICHANGE)  # 刷新桌面

    # 线程化
    def update(self):
        # 创建新的线程去执行网络访问,服务器慢,会阻塞新线程,不影响主线程
        self.thread = Thread(target=self.changeWallpaper,
                        )
        self.thread.start()

    # 切换墙纸
    def changeWallpaper(self):
        """文件夹/图片"""
        print(self.spinBox.value())
        self.play = self.play + 1
        if self.play > 1:  self.play = 0
        while True:
            if self.play == 1:
                self.pushButton_start.setText(QCoreApplication.translate("Form", u"停止轮播", None))
                print(self.filelist[self.imgNo])
                self.label_info.setText("正在显示: {}".format(self.filelist[self.imgNo].split('\\')[-1]))
                self.Windows_img(self.filelist[self.imgNo])

                time.sleep(self.spinBox.value())  # 设置壁纸更换间隔，这里为2秒，根据用户自身需要自己设置秒数
                self.imgNo += 1
                if self.imgNo == len(self.filelist):  # 如果是最后一张图片，则重新到第一张
                    self.imgNo = 0
            else:
                self.pushButton_start.setText(QCoreApplication.translate("Form", u"启动轮播", None))
                return

    # 获取文件列表
    def walkdir(self, rootDir):
        file_list = []
        for root, dirs, files in os.walk(rootDir):
            for file in files:
                # if '.mp4' in file:
                # if '.flv' in file:
                file_list.append(os.path.join(root, file))
                # print(os.path.join(root, file))
        return file_list

    # 打开文件夹
    def setdir(self):
        if self.filelist == []:
            dir = QFileDialog.getExistingDirectory(self, '选择文件夹', '')
            self.lineEdit.setText(dir)
            self.filelist = self.walkdir(dir)
            print('self.filelist: ', self.filelist)
            filenames = [i.split('\\')[-1] for i in self.filelist]
            for file in filenames:
                self.listWidget.addItem(file)
        else:
            dir = QFileDialog.getExistingDirectory(self, '选择文件夹', '')
            self.lineEdit.setText(dir)
            self.filelist_ = self.walkdir(dir)
            for file in self.filelist_:
                if file not in self.filelist:
                    self.filelist.append(file)
                    self.listWidget.addItem(file)

    # 退出
    def quit(self):
        self.play = 0
        if self.checkBox.isChecked():
            self.saveSetting()
        self.close()
        sys.exit()

    # 最小化
    def mini(self):
        self.showMinimized()

    # 重写鼠标事件
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = MyWindow()
    login.show()
    sys.exit(app.exec_())
