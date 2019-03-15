# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TaobaoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    watch_module = scrapy.Field()
    brand = scrapy.Field()
    type = scrapy.Field()
    shop = scrapy.Field()
    sales = scrapy.Field()
    price = scrapy.Field()
    detail_url = scrapy.Field()

#
# def a():
#     print('start')
#     for i in range(5):
#         print("a",i)
#         yield i
# print('out')
# res = a()
# print('out end')
# for j in res:
#     print('in')
#     print(j)
