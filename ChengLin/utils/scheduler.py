


class Scheduler(object):
    def __init__(self):
        self.thread_list = []
        self.window = None
        self.terminate = False  # 点击停止

    def start(self, base_dir, window, fn_start, fn_stop, fn_counter, fn_error_counter):
        self.window = window
        self.terminate = False
        # 1.获取表格中的所有数据,每一行创建一个线程去执行监控
        for row_index in range(window.table_widget.rowCount()):
            # 0/1/2/3
            asin = window.table_widget.item(row_index, 0).text().strip()
            status_text = window.table_widget.item(row_index, 6).text().strip()

            import os
            log_folder = os.path.join(base_dir, 'log')
            if not os.path.exists(log_folder):
                os.makedirs(log_folder)
            log_file_path = os.path.join(log_folder, "{}.log".format(asin))

            # 只有是待执行的时,才创建线程去执行
            if status_text != "待执行":
                continue

            from ChengLin.utils.threads import TaskThread
            # 2.每个线程 执行 & 状态实时的显示在表格中 信号＋回调
            t = TaskThread(self, log_file_path, row_index, asin, window)
            t.start_signal.connect(fn_start)
            t.counter_signal.connect(fn_counter)
            t.error_counter_signal.connect(fn_error_counter)
            t.stop_signal.connect(fn_stop)
            t.start()
            pass

    def stop(self):
        self.terminate = True


# 单例模式
SCHEDULER = Scheduler()