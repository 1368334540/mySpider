# -*- coding: utf-8 -*-
import scrapy


class MyspiderSpidersYoudaoSpider(scrapy.Spider):
    name = 'mySpider.spiders.youdao'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        pass
