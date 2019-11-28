# -*- coding: utf-8 -*-
import scrapy
from steam.items import Product
from scrapy.loader import ItemLoader



class SteamscrapperSpider(scrapy.Spider):
	'''- the spider class that will run the spider and logic'''
	name = 'steamscrapper'
	allowed_domains = ['store.steampowered.com']
	start_urls = ["https://store.steampowered.com/games/#p=0&tab=NewReleases","https://store.steampowered.com/games/#p=1&tab=NewReleases"]

	def parse(self, response):
            l = ItemLoader(item=Product(),response=response)
            l.add_xpath('title', '//div[@class="tab_item_name"]')
            l.add_xpath('price', '//div[@class="discount_final_price"]')