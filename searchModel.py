from PyQt5.Qt import *
import requests
from PyQt5.QtGui import *
import json
import re

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


class kuwosearchThread(QThread):
    def __init__(self,text,model):
        super().__init__()
        self.word=text
        self.model=model

    def run(self):
        if self.word == "":
            print("No word.")
        else:
            all_singers = []  # 放置所有歌手人名
            names = []  # 放置歌曲名字
            all_rid = []  # 放置所有rid，rid是网页所需参数
            for p in range(2):
                url = "http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key={}&pn={}&rn=30&httpsStatus=1&reqId=da11ad51-d211-11ea-b197-8bff3b9f83d2e".format(self.word, str(p + 1))
                response = requests.get(url, headers=headers2)
                response.encoding = response.apparent_encoding
                response = response.json()  # 得到josn字典dict
                try:
                    music_list = response["data"]["list"]  # 得到歌曲列表
                except:
                    pass
                    break
                else:
                    a = 0
                    for music in music_list:
                        singer = music["artist"]  # 歌手名
                        name = music["name"]  # 歌曲名

                        rid = music["musicrid"]  # 取出rid，之后要对这个字符串进行切割
                        index = rid.find('_')
                        rid = rid[index + 1:len(rid)]

                        all_singers.append(singer)  # 将对应信息放到列表中
                        names.append(name)
                        all_rid.append(rid)
                        a = a + 1
            for i in range(len(names)):
                itemProject = QStandardItem(names[i])
                self.model.appendRow(itemProject)
                self.model.setItem(i, 1, QStandardItem(all_singers[i]))
                self.model.setItem(i, 2, QStandardItem(all_rid[i]))


class kugousearchThread(QThread):
    def __init__(self,text,model):
        super().__init__()
        self.word = text
        self.model = model

    def run(self):
        all_singers = []  # 放置所有歌手人名
        names = []  # 放置歌曲名字
        all_rid = []  # 放置所有rid，rid是网页所需参数
        content_url_list = []
        music_listu = [] #url播放列表
        for p in range(1):
            url = "https://songsearch.kugou.com/song_search_v2?callback=jQuery112405886208845288214_1588464073802&keyword={}&page={}&pagesize=30&userid=-1&clientver=&platform=WebFilter&tag=em&filter=2&iscorrection=1&privilege_filter=0&_=1588464073804".format(self.word, str(p + 1))
            response = requests.get(url, headers=headers3).text
            music_list_html = re.findall(r'\((.*)\)', response)[0]
            music_list = json.loads(music_list_html)
            for i in range(len(music_list["data"]["lists"])):
                music_hash = music_list["data"]["lists"][i]["FileHash"]  # 关键字 hash
                music_albumid = music_list["data"]["lists"][i]["AlbumID"]  # 关键字album_id
                all_rid.append(music_albumid)
                information_url = "https://wwwapi.kugou.com/yy/index.php?r=play/getdata&callback=jQuery19101144344902676131_1588093696865&hash={}&album_id={}&dfid=2AHvg428HZSx0oRNWX0prTMo&mid=4b42424f9fa4d173c4601c6b476003f2&platid=4&_=1588093696867".format(music_hash, music_albumid)
                content_url_list.append(information_url)  # 包含歌曲详细信息

            for i in content_url_list:
                url = i
                response = requests.get(url, headers=headers).text
                cut_json = re.findall(r'\((.*)\)', response)[0]  # 格式为json格式
                cut_dict = json.loads(cut_json)  # 转换为字典格式 才能根据键获取值
                try:
                    music_url = cut_dict["data"]["play_url"]  # 歌曲播放地址
                except:
                    pass
                else:
                    music_listu.append(music_url)
                    music_name = cut_dict["data"]["song_name"]  # 歌曲名
                    singer = cut_dict["data"]["author_name"]

                    all_singers.append(singer)
                    names.append(music_name)
            for i in range(len(names)):
                itemProject = QStandardItem(names[i])
                self.model.appendRow(itemProject)
                self.model.setItem(i, 1, QStandardItem(all_singers[i]))
                self.model.setItem(i, 2, QStandardItem(music_listu[i]))