# -*- coding: utf-8 -*-
import scrapy


class MyspiderYoudaospiderSpider(scrapy.Spider):
    name = 'mySpider.youdaoSpider'
    allowed_domains = ['youdao.com']
    start_urls = ['http://youdao.com/']

    def parse(self, response):
        pass
