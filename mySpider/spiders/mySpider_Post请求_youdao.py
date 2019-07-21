# -*- coding: utf-8 -*-
import scrapy


class MyspiderPost请求YoudaoSpider(scrapy.Spider):
    name = 'mySpider.Post请求.youdao'
    allowed_domains = ['youdao,com']
    start_urls = ['http://youdao,com/']

    def parse(self, response):
        pass
