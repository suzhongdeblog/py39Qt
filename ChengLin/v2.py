import os
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QPushButton, QLineEdit, QTableWidget, QTableWidgetItem, QLabel
from PyQt5.QtWidgets import QMessageBox

BASE_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))


STATUS_MAPPING = {
    0: "初始化中",
    1: "待执行",
    2: "正在执行",
    3: "完成并提醒",
    10: "异常并停止",
    11: "初始化失败",
}

class MainWindows(QWidget):
    def __init__(self):
        super().__init__()
        # 控件
        self.txt_asin=None

        # 窗体标题和尺寸
        self.setWindowTitle('NB的xx系统')

        # 窗体的尺寸
        self.resize(1228, 450)

        # 窗体位置
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)

        # 创建布局
        layout = QVBoxLayout()

        layout.addLayout(self.init_header())
        layout.addLayout(self.init_form())
        layout.addLayout(self.init_table())
        layout.addLayout(self.init_footer())

        # 给窗体设置元素的排列方式
        self.setLayout(layout)

    def init_header(self):
        # 1.创建顶部菜单布局
        header_layout = QHBoxLayout()
        # 1.1 创建按钮,加入 header_layout
        btn_start = QPushButton("开始")
        header_layout.addWidget(btn_start)

        btn_stop = QPushButton("停止")
        header_layout.addWidget(btn_stop)

        # 弹簧
        header_layout.addStretch()

        return header_layout

    def init_form(self):
        # 2.创建上面标题布局
        form_layout = QHBoxLayout()

        # 2.1 输入框
        txt_asin = QLineEdit()
        txt_asin.setText("B08166SLDF=100")
        txt_asin.setPlaceholderText("请输入商品ID和价格,例如: B0818JJQQ8=88")
        self.txt_asin = txt_asin
        form_layout.addWidget(txt_asin)

        # 2.2 添加按钮
        btn_add = QPushButton("添加")
        btn_add.clicked.connect(self.event_add_click)
        form_layout.addWidget(btn_add)

        return form_layout

    def init_table(self):
        # 3.创建中间的表格
        table_layout = QHBoxLayout()

        # 3.1 创建表格
        self.table_widget = table_widget = QTableWidget(0,8)
        table_header = [
            {"field": "asin", "text": "ASIN", 'width': 120},
            {"field": "title", "text": "标题", 'width': 150},
            {"field": "url", "text": "URL", 'width': 400},
            {"field": "price", "text": "底价", 'width': 100},
            {"field": "success", "text": "成功次数", 'width': 100},
            {"field": "error", "text": "503次数", 'width': 100},
            {"field": "status", "text": "状态", 'width': 100},
            {"field": "frequency", "text": "频率 (N秒/次)", 'width': 100},
        ]
        for idx, info in enumerate(table_header):
            item = QTableWidgetItem()
            item.setText(info['text'])
            table_widget.setHorizontalHeaderItem(idx,item)
            table_widget.setColumnWidth(idx, info['width'])

        # 3.2 初始化表格数据
        # 读取数据文件
        import json
        file_path = os.path.join(BASE_DIR, "db", "db.json")
        with open(file_path, mode='r', encoding='utf-8') as f:
            data = f.read()
        data_list = json.loads(data)


        current_row_count = table_widget.rowCount() # 当前表格有多少行
        for row_list in data_list:
            table_widget.insertRow(current_row_count)

            # row_list    # ['B08166SLDF', 'AMD er', 'https://www.amazon.com/gp/offer-listing/B08166SLDF/ref=dp_olp_all_mbc?ie=UTF8&condition=new', 300.0, 0, 166, 1, 5]
            # 写真是数据
            for i, ele in enumerate(row_list):
                ele = STATUS_MAPPING[ele] if i == 6 else ele
                cell = QTableWidgetItem(str(ele))
                if i in [0, 4, 5, 6]:
                    # 不可修改
                    cell.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                table_widget.setItem(current_row_count, i, cell)

            current_row_count += 1

        table_layout.addWidget(table_widget)

        return table_layout

    def init_footer(self):
        # 2.底部菜单
        footer_layout = QHBoxLayout()

        label_status = QLabel("未检测")
        footer_layout.addWidget(label_status)

        footer_layout.addStretch()

        btn_reinit = QPushButton("重新初始化")
        footer_layout.addWidget(btn_reinit)

        btn_recheck = QPushButton("重新检测")
        footer_layout.addWidget(btn_recheck)

        btn_reset_count = QPushButton("次数清零")
        footer_layout.addWidget(btn_reset_count)

        btn_delete = QPushButton("删除检测项")
        footer_layout.addWidget(btn_delete)

        btn_alert = QPushButton("SMTP报警配置")
        footer_layout.addWidget(btn_alert)

        btn_proxy = QPushButton("代理IP")
        footer_layout.addWidget(btn_proxy)

        return footer_layout

    # 点击添加按钮
    def event_add_click(self):
        # 1.获取输入框中的内容
        text = self.txt_asin.text()
        text = text.strip()
        if not text:
            QMessageBox.warning(self, "错误", "商品的ASIN输入错误")
            return
        # B08166SLDF=100
        asin, price = text.split("=")
        price = float(price)

        # 2.加入到表格中 (型号,底价)
        new_row_list = [asin, "", "", price, 0, 0, 0, 5]

        current_row_count = self.table_widget.rowCount()  # 当前表格有多少行
        self.table_widget.insertRow(current_row_count)
        for i, ele in enumerate(new_row_list):
            ele = STATUS_MAPPING[ele] if i == 6 else ele
            cell = QTableWidgetItem(str(ele))
            if i in [0, 4, 5, 6]:
                # 不可修改
                cell.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.table_widget.setItem(current_row_count, i, cell)

        # 3.发送请求自动获取标题 (爬虫获取数据)
        # 注意: 不能在主线程中做爬虫的事,创建一个线程去做爬虫,爬取到数据再更新到窗体应用 (信号)。
        from utils.threads import NewTaskThread
        thread = NewTaskThread(current_row_count,asin,self)
        thread.success.connect(self.init_task_success_callback)
        thread.success.connect(self.init_task_error_callback)
        thread.start()
        pass
    def init_task_success_callback(self, row_index, asin, title, url):
        # 更新标题
        cell_title = QTableWidgetItem(title)
        self.table_widget.setItem(row_index, 1, cell_title)

        # 更新URL
        cell_url = QTableWidgetItem(url)
        self.table_widget.setItem(row_index, 2, cell_url)

        # 更新状态
        cell_status = QTableWidgetItem(STATUS_MAPPING[1])
        cell_status.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.table_widget.setItem(row_index, 6, cell_status)

        # 输入框清空
        self.txt_asin.clear()

    def init_task_error_callback(self, row_index, asin, title, url):
        # 更新标题
        cell_title = QTableWidgetItem(title)
        self.table_widget.setItem(row_index, 1, cell_title)

        # 更新URL
        cell_url = QTableWidgetItem(url)
        self.table_widget.setItem(row_index, 2, cell_url)

        # 更新状态
        cell_status = QTableWidgetItem(STATUS_MAPPING[11])
        cell_status.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.table_widget.setItem(row_index, 6, cell_status)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindows()
    window.show()
    sys.exit(app.exec_())