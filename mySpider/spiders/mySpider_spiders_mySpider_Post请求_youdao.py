# -*- coding: utf-8 -*-
import scrapy


class MyspiderSpidersMyspiderPost请求YoudaoSpider(scrapy.Spider):
    name = 'mySpider.spiders.mySpider_Post请求_youdao'
    allowed_domains = ['youdao.com']
    start_urls = ['http://youdao.com/']

    def parse(self, response):
        pass
