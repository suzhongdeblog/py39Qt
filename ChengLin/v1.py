import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget


class MainWindows(QWidget):
    def __init__(self):
        super().__init__()

        # 窗体标题和尺寸
        self.setWindowTitle('NB的xx系统')

        # 窗体的尺寸
        self.resize(980, 450)

        # 窗体位置
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindows()
    window.show()
    sys.exit(app.exec_())