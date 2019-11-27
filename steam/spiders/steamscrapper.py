# -*- coding: utf-8 -*-
import scrapy


class SteamscrapperSpider(scrapy.Spider):
    name = 'steamscrapper'
    allowed_domains = ['https://store.steampowered.com/games/#p=0']
    start_urls = ['http://https://store.steampowered.com/games/#p=0/']

    def parse(self, response):
        pass
