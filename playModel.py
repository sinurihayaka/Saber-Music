import webbrowser
from PyQt5.Qt import *
import requests
from PyQt5.QtGui import *
import json

headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"}

headers1 = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': '_ga=GA1.2.1500987479.1595755923; _gid=GA1.2.568444838.1596065504; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1595755923,1596065505; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1596076178; kw_token=P5XA2TZXG9',
    'csrf': 'P5XA2TZXG9',
    'Host': 'www.kuwo.cn',
    'Referer': 'http://www.kuwo.cn/search/list?key=%E5%A4%95%E9%98%B3%E7%BA%A2',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
}

headers2 = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': '_ga=GA1.2.1500987479.1595755923; _gid=GA1.2.568444838.1596065504; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1595755923,1596065505; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1596078189; _gat=1; kw_token=IJATWHHGI8',
    'csrf': 'IJATWHHGI8',
    'Host': 'www.kuwo.cn',
    'Referer': 'http://www.kuwo.cn/search/list?key=%E6%A2%A6%E7%9A%84%E5%9C%B0%E6%96%B9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',

}

headers3 = {"cookie": "kg_mid=4b42424f9fa4d173c4601c6b476003f2; kg_dfid=2AHvg428HZSx0oRNWX0prTMo; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1587913892,1588084386; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; kg_mid_temp=4b42424f9fa4d173c4601c6b476003f2; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1588093697",
           "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}

class playThread(QThread):
    def __init__(self,stand,item,textedit):
        super().__init__()
        self.stand=stand
        self.item=item
        self.textedit = textedit

    def run(self):
        if self.stand == "酷我音乐(推荐)":
            urlm = 'http://www.kuwo.cn/api/v1/www/music/playUrl?mid={}&type=convert'.format(self.item)
            resp = requests.get(url=urlm, headers=headers)
            dd = json.dumps(resp.text)
            resp = json.loads(dd)
            resp = json.loads(resp)["data"]["url"]
            self.textedit.append("酷我音乐(推荐)播放："+resp)
            webbrowser.open_new_tab(resp)
        elif self.stand == "酷狗音乐":
            self.textedit.append("酷狗音乐播放：" +self.item)
            webbrowser.open_new_tab(self.item)