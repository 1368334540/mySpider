# -*- coding: utf-8 -*-
import scrapy
import  re
from mySpider.items import MyspiderItem

class MusicspiderSpider(scrapy.Spider):
    name = 'musicSpider'#爬虫名称
    allowed_domains = ["www.130v.com/"]  #爬虫网页范围  http://要去掉
    start_urls = ['http://www.130v.com/'] #起始url
# 处理响应内容的方法，写入本地
    def parse(self, response):
        # filename="music.html"
        data = response.body.decode(encoding="utf-8", errors="ignore") #获取响应内容  decode()是解码的意思，从html字节码解码成二进制
        # open(filename,"wb").write(data)#写入本地
    #<a href='/play/16315.html' target="play">06_8号交响曲</a>
        pat1 = re.compile(r'<a href=\'.*?\' target="play">(.*?)</a>')
        pat2 = re.compile(r"<a href='(.*?)' target=\"play\"")
        title = re.findall(pat1,data)
        songUrl=re.findall(pat2,data)
        # items=[]
        for  i  in range(0,len(title)):
            item = MyspiderItem()
            item["title"] = title[i]
            item["songUrl"] ="http://www.130v.com/"+ songUrl[i]
            yield item   #每构建一个item生成器就返回给Pipeline 相当多线程啦
        #     items.append(item)
        # return items
    #返回数据人看不到，可以手动生成Json文件查看 。
     #scrap crawl  musicSpider （类名） -o  music,json（json文件名）
