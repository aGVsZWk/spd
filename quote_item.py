# -*- coding: utf-8 -*-
# @Author  : HeLei
# @Time    : 2023/12/8 11:30
# @File    : QuoteItem.py
import scrapy


# from scrapy.loader import ItemLoader
# from myproject.items import Product
#
# def parse(self, response):
#     l = ItemLoader(item=Product(), response=response)
#     l.add_xpath('name', '//div[@class="product_name"]')
#     l.add_xpath('name', '//div[@class="product_title"]')
#     l.add_xpath('price', '//p[@id="price"]')
#     l.add_css('stock', 'p#stock]')
#     l.add_value('last_updated', 'today') # you can also use literal values
#     return l.load_item()


class Quote(scrapy.Item):
    text = scrapy.Field()
    author = scrapy.Field()


quote = Quote(text="那些听不见音乐的人认为那些跳舞的人疯了。", author=None)
print(quote)

# curl 'https://v2.jinrishici.com/one.json' \
#   -H 'authority: v2.jinrishici.com' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -H 'origin: chrome-extension://eldcinofoklpfhaanlhmkmadehfgcnon' \
#   -H 'pragma: no-cache' \
#   -H 'sec-ch-ua: "Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: empty' \
#   -H 'sec-fetch-mode: cors' \
#   -H 'sec-fetch-site: cross-site' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36' \
#   --compressed