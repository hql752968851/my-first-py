# -*- coding: utf-8 -*-
import scrapy
import sys



class StockstarSpider(scrapy.Spider):
    name = 'stockStar'
    allowed_domains = ['stockstar.com']
    start_urls = ['http://quote.stockstar.com/stock/sha.shtml']

    def parse(self, response):
        item=StockspiderItem()

        pass
