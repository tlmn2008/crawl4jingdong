# -*- coding: utf-8 -*-
import scrapy
from taobao.items import TaobaoItem


class MytaobaoSpider(scrapy.Spider):
    name = 'mytaobao'
    allowed_domains = ['taobao.com','tmall.com']
    # start_urls = 'https://s.taobao.com/search?q=%E5%84%BF%E7%AB%A5%E7%94%B5%E8%AF%9D%E6%89%8B%E8%A1%A8&s=0'
    base_url = 'https://s.taobao.com/search?q=python&s=0'
    page = 1
    start_urls = [base_url]
# 1: 'https://s.taobao.com/search?q=python&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s=0'
# 2: 'https://s.taobao.com/search?q=python&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s=44'
# 4: 'https://s.taobao.com/search?q=python&bcoffset=-3&ntoffset=-3&p4ppushleft=1%2C48&s=132'
# 10:'https://s.taobao.com/search?q=python&bcoffset=-21&ntoffset=-21&p4ppushleft=1%2C48&s=396'
# 15:'https://s.taobao.com/search?q=python&bcoffset=-36&ntoffset=-36&p4ppushleft=1%2C48&s=616'

    def start_requests(self):
       # key_words = self.setting['KEY_WORDS']
       # key_words = parse.quote(key_words,' ').replace(' ','+')
       # page_num = self.setting['PAGE_NUM']
       # one_page_count = self.setting['ONE_PAGE_COUNT']
       # for i in range(page_num):
       #     url = self.base_url % (key_words,i*one_page_count)
       #     yield scrapy.Request(url,callback=self.parse)
#     def start_requests(self):
#         print("this is start_requests")
        print('this is start_requests')
        yield scrapy.Request(url=self.base_url, callback=self.parse, meta={'page': self.page}, dont_filter=True)
        print('end of start_requests')

    def parse(self, response):
        print('this is parse')
        print(response)
        div_list = response.xpath("//div[@class='grid g-clearfix']/div[1]/div")
        print(div_list)
        for div in div_list:
            # item = TaobaoItem()
            # item["price"] = div.xpath(".//div[@class='price g_price g_price-highlight']/@strong").extract_first()
            # item["detail_url"] = div.xpath(".//div[@class='row row-2 title']/a[@class='J_ClickStat']/@href").extract_first()
            # item["shop"] = div.xpath(".//div[@class='row row-3 g-clearfix']//a[@class='shopname J_MouseEneterLeave J_ShopInfo']/span[last()]").extract_first()
            goods_link = div.xpath(".//div[@class='item J_MouserOnverReq']/div[class='pic-box J_MouseEneterLeave J_PicBox']/div[class='pic-box-inner']/div[class='pic']/@href")
            print("@@@@@@@@@@@@@ href is {}".format(goods_link))
            # yield scrapy.Request(url=self.base_url, callback=self.parse, meta={'page': self.page}, dont_filter=True)
        # if self.page < 100:
        #     self.page += 1
        #     print(self.page)
        #     yield scrapy.Request(url=self.base_url,callback=self.parse,meta={'page':self.page},dont_filter=True)