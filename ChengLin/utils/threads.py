import requests
from bs4 import BeautifulSoup
from PyQt5.QtCore import QThread, pyqtSignal

HOST = "https://www.amazon.com/"
HOST_ASIN_TPL = "{}{}".format(HOST, "gp/product/")
HOST_TASK_LIST_TPL = "{}{}".format(HOST, "gp/offer-listing")

# https://www.amazon.com/gp/product/B07YN82X3B/


class NewTaskThread(QThread):

    # 信号，触发信号，更新窗体中的数据
    success = pyqtSignal(int, str, str, str)
    error = pyqtSignal(int, str, str, str)

    def __init__(self,row_index, asin, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.row_index = row_index
        self.asin = asin

    def run(self):
        """ 具体线程应该做的事"""
        try:
            res = requests.get(
                url="https://www.amazon.com/gp/product/{}/".format(self.asin),
                headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
                    "pragma": "no-cache",
                    "upgrade-insecure-requests": "1",
                    "cache-control": "no-cache",
                    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7",
                    "accept-encoding": "gzip,deflate,br",
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
                }
            )
            if res.status_code != 200:
                raise Exception("初始化失败")

            soup = BeautifulSoup(res.text,'lxml')
            title = soup.find(id="productTitle").text.strip()
            tpl = "https://www.amazon.com/gp/product/ajax/ref=dp_aod_ALL_mbc?asin={}&m=&qid=&smid=&sourcecustomerorglistid=&sourcecustomerorglistitemid=&sr=&pc=dp&experienceId=aodAjaxMain"
            url = tpl.format(self.asin)
            # 获取到title和url, 将这个信息填写到 表格上 & 写入文件中。
            self.success.emit(self.row_index, self.asin, title, url)
        except Exception as e:
            title = "监控项 {} 添加失败。".format(self.asin)
            self.error.emit(self.row_index, self.asin, title, str(e))
