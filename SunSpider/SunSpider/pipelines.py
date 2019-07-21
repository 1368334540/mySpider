# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

#记得给优先级 还有robot不要！
class SunspiderPipeline(object):
    def __init__(self):
        self.filename=open(r"sun.txt","a",encoding="utf-8")
    def process_item(self, item, spider):
        content=str(item)+"\n"
        self.filename.write(content)
        return item
    # def close_spider(self):
    #     self.filename.close()