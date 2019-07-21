# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import  json
#管道一个，负责item的后期处理或保存  如果是多个对象 就是 多个管道，不管怎杨，都需要在Setting设置管道优先级
class MyspiderPipeline(object):
    def __init__(self):
        self.file = open('music.text', 'a', encoding='utf-8')
        # self.file.write("[")     # 把item数据写入里面 a是追加，多线程w可能会覆盖， 多线程不安全写入不能用w
        #管道每次收到item后执行的方法
    def process_item(self, item, spider):
        # print("----------"+item)
        # content = str(item)+"\n"  str()没用
        # dict_item = dict(item)
        #         #
        #         # json_item = json.dumps(dict_item)  #dumps讲字典转成json格式
        #         # self.file.write(json_item)

        content = str(item) + "\n"
        self.file.write(content)
        return item
    #当爬取结束时执行的方法

    def close_spider(self,spider):
        self.file.close()
    #     #     self.spider.close()