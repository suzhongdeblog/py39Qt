import sys
from PySide2.QtCore import Qt
from PySide2.QtGui import QCursor
from PySide2.QtWidgets import QApplication, QMainWindow
from login import *




class MyWindow(QMainWindow, Ui_Form):

    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.change_widget2()
        # 链接到函数
        self.pushButton.clicked.connect(self.change_widget2)
        self.pushButton_2.clicked.connect(self.change_widget3)
        self.pushButton_4.clicked.connect(self.quit)
        self.pushButton_5.clicked.connect(self.mini)

    # 退出
    def quit(self):
        self.close()
        sys.exit()

    # 最小化
    def mini(self):
        self.showMinimized()

    # 窗口切换
    def change_widget3(self):
        self.widget_2.hide()
        self.widget_3.show()

    def change_widget2(self):
        self.widget_3.hide()
        self.widget_2.show()


    # 重写鼠标事件
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos() 
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor)) 

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))




if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = MyWindow()
    login.show()
    sys.exit(app.exec_())
