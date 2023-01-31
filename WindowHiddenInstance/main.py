from PyQt5.Qt import *
import sys


class Window(QMainWindow):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.resize(500, 500)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setStyleSheet("background-color: rgb(17, 17, 19);")

    # 鼠标进入事件    鼠标移到窗口上将会执行这个事件
    def enterEvent(self, evt):
        # 判断y坐标是否等于 -498 是的话就说明它在外边，哪我们开启动画让他跑回来
        if self.y() == -498:
            # 开启动画
            animation = QPropertyAnimation(self, b"pos", self)
            animation.setStartValue(QPoint(self.x(), self.y()))  # 这是动画起始位置
            animation.setEndValue(
                QPoint(self.x(), 0))  # 这是结束位置  x 不变， 让y变成负数就会跑到屏幕外边去， 我的高是500，设置了498，剩下2，不要全部设置成500， 不然鼠标进不去窗口，就移不出来
            animation.setDuration(200)  # 设置动画时长
            animation.start()  # 启动动画

        print("鼠标进来了")

    # 鼠标离开事件    鼠标从窗口上移出将会执行这个事件
    def leaveEvent(self, evt):
        # 鼠标移出去，我们判断它的y坐标是否等于或小于0  如果是 说明窗口就在屏幕边缘 那我们就开启动画让它跑到屏幕外边去
        if self.y() <= 0:
            # 开启动画
            animation = QPropertyAnimation(self, b"pos", self)
            animation.setStartValue(QPoint(self.x(), self.y()))     # 这是动画起始位置
            animation.setEndValue(QPoint(self.x(), -498))   #  这是结束位置  x 不变， 让y变成负数就会跑到屏幕外边去， 我的高是500，设置了498，剩下2，不要全部设置成500， 不然鼠标进不去窗口，就移不出来
            animation.setDuration(200)  # 设置动画时长
            animation.start()   # 启动动画
        print("鼠标出去了")

    def mousePressEvent(self, evt):
        if evt.button() == Qt.LeftButton:
            self.switch = True
        else:
            self.switch = False

        self.mouse_x = evt.globalX()
        self.mouse_y = evt.globalY()
        self.window_x = self.x()
        self.window_y = self.y()

    def mouseMoveEvent(self, evt):
        if self.switch:
            move_x = evt.globalX() - self.mouse_x
            move_y = evt.globalY() - self.mouse_y

            vector_x = self.window_x + move_x
            vector_y = self.window_y + move_y
            self.move(vector_x, vector_y)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()

    window.show()

    sys.exit(app.exec_())
