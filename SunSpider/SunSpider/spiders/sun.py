# -*- coding: utf-8 -*-
import scrapy
from SunSpider.items import SunspiderItem


class SunSpider(scrapy.Spider):
    name = 'sun'
    allowed_domains = ['wz.sun0769.com']  #网页范围是 官网首页 #这里后面没有"/" 我犯下了错误！
    offset=0
    url= "http://wz.sun0769.com/index.php/question/report?page="  #（n-1）*30  自动翻页，
    start_urls = [url+str(offset)]

    # 所以定义要这样的url
#先得到页面的title和url详情
    def parse(self, response):#拿到每个帖子的url，结果返回列表       #extract()函数拿到xpath清洗的内容                 #这里xpath要细心 不要多加"]["
        links =response.xpath('//div[@class="greyframe"]//table//tr//tr//td/a[@class="news14"]/@href').extract()  #已经拿到body ，直接洗出url和titile
        for link in links:  #发送每一个帖子的请求，用self.parse_item来处理
            yield scrapy.Request(link,callback=self.parse_item)     #发送请求到详细的url 回调函数记得没有括号！
        if self.offset <= 150:
            self.offset+=30
            #重新发送请求 继续爬下一页
            yield scrapy.Request(self.url+str(self.offset),callback=self.parse)


    #处理每个帖子里的内容，放进item里输送管道
    def parse_item(self,response):#text()表示拿xpath最后一个标签里面的内容 ，拿记得要函数extract()
        item = SunspiderItem()  #生成对象记得要加括号！ 我又没加
        item["content"]="".join(response.xpath('//td[@class="txt16_3"]//div/text()').extract())# 列表字符串用指定的字符连接成一个新列表
        item["url"] = response.url             #记得！ 先extract拿出所有字符串了以后在join（）用指定的字符拼接成新的字符串  class一定要仔细对准，很容易出错！！！！
        item["title"]=response.xpath('//span[@class="niae2_top"]/text()').extract()[0]
        #item里面的属性，我两个都写错了！，以后直接复制过来！以防出错！概论非常之高！
        yield item   #返回是yiedl  记得啊！

