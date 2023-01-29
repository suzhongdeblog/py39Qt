


class Scheduler(object):
    def __init__(self):
        self.thread_list = []
        self.window = None
        self.terminate = False  # 点击停止

    def start(self, window, fn_start, fn_counter):
        self.window = window
        self.terminate = False
        # 1.获取表格中的所有数据,每一行创建一个线程去执行监控
        for row_index in range(window.table_widget.rowCount()):
            # 0/1/2/3
            asin = window.table_widget.item(row_index, 0).text().strip()
            status_text = window.table_widget.item(row_index, 6).text().strip()

            # 只有是待执行的时,才创建线程去执行
            if status_text != "待执行":
                continue

            from ChengLin.utils.threads import TaskThread
            # 2.每个线程 执行 & 状态实时的显示在表格中 信号＋回调
            t = TaskThread(row_index, asin, window)
            t.start_signal.connect(fn_start)
            t.counter_signal.connect(fn_counter)
            t.start()
            pass

    def stop(self):
        pass


# 单例模式
SCHEDULER = Scheduler()