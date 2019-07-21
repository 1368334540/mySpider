# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

#记得给robot注释，记得给管道解除注释设置优先级，越小越优先300就好！
class SunspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    content = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()

