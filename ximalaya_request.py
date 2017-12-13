# -*- coding: UTF-8 -*-
import requests#网络请求模块

import re #使用正则表达式

import urllib #用于下载音频

import time

header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}

'''
喜马拉雅的每一个网址,都是有一定的规律:
http://www.ximalaya.com/4932085/sound/10494941/
http://www.ximalaya.com/4932085/sound/10494942/
http://www.ximalaya.com/4932085/sound/10524833/
后边的只是数字不同.我们需要爬这些数字
'''
#number = re.findall('href="/4932085/sound/(.*?)/" hashlink title',html.text)
#获取数字字段,用于构造下载歌曲的网址
pages =[]
for ii in range(1,18):
    url = 'http://www.ximalaya.com/4932085/album/3160816?page='+str(ii)
    html = requests.get(url, headers=header)  # 返回网页源代码
    data = re.findall('href="/4932085/sound/(.*?)/" hashlink title', html.text)
    pages.extend(data) #extend append

datas = list(set(pages)) #去重操作

for m in datas[:10]:
    #拼凑网址
    time.sleep(2)
    js = 'http://www.ximalaya.com/tracks/'+m+'.json'
    html1 = requests.get(js,headers=header)#请求网址
    m4a = html1.json()['play_path_64']#转化为json格式
    urllib.request.urlretrieve(m4a,'/Users/xiahngjin/Desktop/ximalaya/'+m+'.m4a',)