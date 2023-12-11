# -*- coding: utf-8 -*-
# @Author  : HeLei
# @Time    : 2023/12/11 14:06
# @File    : bk_spider.py
import time
import scrapy


class ScrpayprojectItem(scrapy.Item):
    #  define  the  fields  for  your  item  here  like:
    author = scrapy.Field()
    start = scrapy.Field()
    buy = scrapy.Field()
    pass


# 解析贝壳二手房页面的房源图片及标题
class TotalBeikeSpider(scrapy.Spider):
    name = 'beike'
    # allowed_domains = ['www.beike.com']
    start_urls = ['https://dl.ke.com/ershoufang/']
    # start_urls = ['https://dl.ke.com/ershoufang/102105500760.html']

    page_num = 1

    def parse_detail(self, response):
        """
        爬取深一层的页面的数据
        """
        item = response.meta['item']
        start = response.xpath('//*[@id="introduction"]/div/div/div[2]/div[2]/ul/li[1]/text()').extract()
        buy = response.xpath('//*[@id="introduction"]/div/div/div[2]/div[2]/ul/li[3]/text()').extract()
        item['start'] = start[0].strip()
        item['buy'] = buy[0].strip()
        yield item  # 将item提交给管道

    def parse(self, response):
        divList = response.xpath('/html/body/div[1]/div[4]/div[1]/div[4]/ul/li[1]')
        title = []
        for div in divList:
            title = div.xpath('//ul[@class="sellListContent"]//img[@class="lj-lazy"]/@title').extract()
            hreflist = div.xpath('//ul[@class="sellListContent"]//div[@class="title"]//a[@data-click-event="SearchClick"]/@href').extract()
            for ind, it in enumerate(title):
                item = ScrpayprojectItem()
                item['author'] = it  # author属性必须在items.py中声明
                detail_url = hreflist[ind]
                # print(detail_url)
                # print(detail_url)
                # 爬取深一层的页面的数据
                yield scrapy.Request(url=detail_url, callback=self.parse_detail, meta={'item': item})
                yield item  # 将item提交给管道
        if self.page_num <= 100:
            new_url = 'https://dl.ke.com/ershoufang/pg'+str(self.page_num)+'/'
            print(new_url)
            self.page_num += 1
            # 手动请求发送：callback回调函数是专门用作与数据解析
            yield scrapy.Request(url=new_url, callback=self.parse)


class mysqlPipeline:
    conn = None
    cursor = None
    # 重写父类的一个方法，该方法只在开始爬虫的时候调用一次
    def open_spider(self,spider):
        print('开始写入数据库……')
        # self.conn = pymysql.Connect(host="39.107.142.167", port=3306,user='root',password='root@mule123',db='test')

    # 该方法每接到一个item就会调用一次
    def process_item(self, item, spider):
        self.cursor = self.conn.cursor()
        sql = "insert into test (author,start,buy) values ('"+item["author"]+"','"+item["start"]+"','"+item["buy"]+"')"
        print(sql)
        try:
            print(sql)
            # print(sql)
            # 执行 插入语句
            # self.cursor.execute(sql)
            # 数据库提交
            # self.conn.commit()
        except Exception as e:
            # print("数据库回滚")
            # 数据库回滚
            # self.conn.rollback()
            pass
        return item

    # 重写父类的一个方法，该方法只在结束爬虫的时候调用一次
    def close_spider(self, spider):
        print('结束写入数据库……')
        # self.conn.close()
        # self.cursor.close()
