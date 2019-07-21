# -*- coding: utf-8 -*-
import scrapy


class YoudaoSpider(scrapy.Spider):
    name = 'youdao'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        pass
