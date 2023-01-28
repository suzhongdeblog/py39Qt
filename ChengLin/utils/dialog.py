import os
import json

from PyQt5.QtWidgets import QVBoxLayout, QDialog, QPushButton, QLabel, QLineEdit, QMessageBox, QTextEdit, QWidget, QDesktopWidget, QHBoxLayout

from PyQt5.QtCore import Qt

class AlertDialog(QDialog):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.field_dict = {}
        self.init_ui()

    def init_ui(self):
        """
        初始化对话框
        :return:
        """
        self.setWindowTitle("报警邮件配置")
        self.resize(300, 270)

        layout = QVBoxLayout()

        form_data_list = [
            {"title": "SMTP服务器", "filed": "smtp"},
            {"title": "发件箱", "filed": "from"},
            {"title": "密码", "filed": "pwd"},
            {"title": "收件人 (多个用逗号分隔)：", "filed": "to"},
        ]

        # 读取文件中的配置
        old_alert_dict = {}
        alert_file_path = os.path.join("db", 'alert.json')
        if os.path.exists(alert_file_path):

            file_object = open(os.path.join("db", 'alert.json'),mode='r', encoding='utf-8')
            old_alert_dict = json.load(file_object)
            file_object.close()

        for item in form_data_list:
            lbl = QLabel()
            lbl.setText(item['title'])
            layout.addWidget(lbl)

            txt = QLineEdit()
            layout.addWidget(txt)

            filed = item['filed']
            if old_alert_dict and filed in old_alert_dict:
                txt.setText(old_alert_dict[filed])
            self.field_dict[item['filed']] = txt

        btn_save = QPushButton("保存")
        btn_save.clicked.connect(self.event_save_click)
        layout.addWidget(btn_save, 0, Qt.AlignRight)

        layout.addStretch(1)
        self.setLayout(layout)

    def event_save_click(self):
        data_dict = {}
        for key, filed in self.field_dict.items():
            value = filed.text().strip()
            if not value:
                QMessageBox.warning(self, "错误", "邮件报警项不能为空")
                return
            data_dict[key] = value

        # {'smtp': '1', 'from': '2', 'pwd': '3', 'to': '4'}
        print(data_dict)

        file_object = open(os.path.join("db", 'alert.json'),mode='w', encoding='utf-8')
        json.dump(data_dict,file_object)
        file_object.close()

        # 关闭对话框
        self.close()