from PyQt5.Qt import *
import sys
from untitled import Ui_MainWindow


class Window(QMainWindow):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.state = "start"
        self.ui.pushButton_6.clicked.connect(self.Begin)
        self.timer = QTimer()
        self.timer.timeout.connect(self.cao)

        self.timer_2 = QTimer()
        self.timer_2.timeout.connect(self.cao2)
        self.timer_2.start(1000)

    def cao(self):
        self.ui.horizontalSlider.setValue(self.ui.horizontalSlider.value() + 1)

    def cao2(self):
        self.ui.stackedWidget.setCurrentIndex((self.ui.stackedWidget.currentIndex() + 1) % self.ui.stackedWidget.count())
        result = self.ui.widget_2.findChildren(QRadioButton)
        result[self.ui.stackedWidget.currentIndex()].setChecked(True)

    def Begin(self):
        if self.state == "start":
            self.ui.pushButton_6.setIcon(QIcon(":/icon/image/暂停_pause-one.png"))
            self.state = "stop"
            self.timer.start(100)
        else:
            self.ui.pushButton_6.setIcon(QIcon(":/icon/image/播放_play.png"))
            self.state = "start"
            self.timer.stop()

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