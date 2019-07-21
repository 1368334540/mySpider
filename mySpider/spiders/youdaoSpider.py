# -*- coding: utf-8 -*-
import scrapy


class YoudaospiderSpider(scrapy.Spider):
    name = 'youdaospider'
    allowed_domains = ['youdao.com']
    start_urls = ['http://youdao.com/']

    def parse(self, response):
        pass
