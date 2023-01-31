from PyQt5.Qt import *
import sys
from untitled import Ui_MainWindow


class Window(QMainWindow):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_8.clicked.connect(self.slideLeftMenu)
        self.ui.comboBox.currentTextChanged.connect(self.cao)

        self.ui.pushButton.clicked.connect(lambda: self.ui.comboBox.setCurrentIndex(0))
        self.ui.pushButton_2.clicked.connect(lambda: self.ui.comboBox.setCurrentIndex(1))
        self.ui.pushButton_3.clicked.connect(lambda: self.ui.comboBox.setCurrentIndex(2))
        self.ui.pushButton_4.clicked.connect(lambda: self.ui.comboBox.setCurrentIndex(3))
        self.ui.pushButton_5.clicked.connect(lambda: self.ui.comboBox.setCurrentIndex(4))
        self.ui.pushButton_6.clicked.connect(lambda: self.ui.comboBox.setCurrentIndex(5))
        self.ui.pushButton_7.clicked.connect(lambda: self.ui.comboBox.setCurrentIndex(6))

    def cao(self):
        name = self.ui.comboBox.currentText()
        if name == "水果":
            self.ui.stackedWidget.setCurrentIndex(self.ui.comboBox.currentIndex())
            self.ui.pushButton.click()
        elif name == "服装":
            self.ui.stackedWidget.setCurrentIndex(self.ui.comboBox.currentIndex())
            self.ui.pushButton_2.click()
        elif name == "手机":
            self.ui.stackedWidget.setCurrentIndex(self.ui.comboBox.currentIndex())
            self.ui.pushButton_3.click()
        elif name == "化妆品":
            self.ui.stackedWidget.setCurrentIndex(self.ui.comboBox.currentIndex())
            self.ui.pushButton_4.click()
        elif name == "护肤品":
            self.ui.stackedWidget.setCurrentIndex(self.ui.comboBox.currentIndex())
            self.ui.pushButton_5.click()
        elif name == "椅子":
            self.ui.stackedWidget.setCurrentIndex(self.ui.comboBox.currentIndex())
            self.ui.pushButton_6.click()
        elif name == "桌子":
            self.ui.stackedWidget.setCurrentIndex(self.ui.comboBox.currentIndex())
            self.ui.pushButton_7.click()


    def slideLeftMenu(self):
        width = self.ui.frame.width()
        if width == 35:
            newWidth = 100
            self.ui.pushButton_8.setIcon(QIcon(":/icon/images/双左_double-left.png"))
        else:
            newWidth = 35
            self.ui.pushButton_8.setIcon(QIcon(":/icon/images/双右_double-right.png"))
        animation = QPropertyAnimation(self.ui.frame, b"minimumWidth", self)
        animation.setStartValue(width)
        animation.setEndValue(newWidth)
        animation.setDuration(200)
        animation.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()

    window.show()

    sys.exit(app.exec_())