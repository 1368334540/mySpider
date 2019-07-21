# -*- coding: utf-8 -*-
import scrapy
import re

class YoudaoSpider(scrapy.Spider):
    global key
    key = input("请输入要翻译的内容：")
    name = 'youdao'
    allowed_domains = ['youdao.com']
    # start_urls = ['http://youdao.com/']
    def start_requests(self):
        header={"User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, l"
            "ike Gecko) Chrome/55.0.2883.87 Safari/537.36"}
        url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
        #生成表单请求信息
        yield scrapy.FormRequest(
            url=url,
            headers=header,
            formdata={
                "i": key,
                "from": "AUTO",
                "to": "AUTO",
                "smartresult": "dict",
                "client": "fanyideskweb",
                "salt": "15503049709404",
                "sign": "3da914b136a37f75501f7f31b11e75fb",
                "ts": "1550304970940",
                "bv": "ab57a166e6a56368c9f95952de6192b5",
                "doctype": "json",
                "version": "2.1",
                "keyfrom": "fanyi.web",
                "action": "FY_BY_REALTIME",
                "typoResult": "false"
            },
            callback=self.parse  #非常容易出错的地方！这里回调函数不能有括号！
        )
    def parse(self, response):

        print("==================================================================")
        print(response.body)
        #"tgt": "Beijing"}
        data = response.body.decode()  #decode()把字节码转成字符串二进制类型
        pat = re.compile('"tgt":"(.*?)"')
        result=re.search(pat,data).group(1)  #拿到第一个括号里的内容
        print("==================================================================")
        print(key+":\t"+result)