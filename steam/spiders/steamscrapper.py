# -*- coding: utf-8 -*-
import scrapy


class SteamscrapperSpider(scrapy.Spider):
	'''- the spider class that will run the spider and logic'''
	name = 'steamscrapper'
	allowed_domains = ['store.steampowered.com']
	start_urls = ["https://store.steampowered.com/games/#p=0&tab=NewReleases","https://store.steampowered.com/games/#p=1&tab=NewReleases"]

	custom_settings = {'FEED_URI': "scrapper_%(time)s.json", 'FEED_FORMAT': 'json'}
	def parse(self, response):
		print("processing:" + response.url)
		product_name = response.css('.tab_item_name::text').extract()
		prodcut_price = response.css('.discount_final_price::text').extract()
		row_data = zip(product_name, prodcut_price)

		for item in row_data:
			scraped_info = {'page': response.url,'product_name':item[0],'price_range': item[1],}
			yield scraped_info
	'''
        	the yeild keyword is used whenever you are defining a generator function. a 
        	generator function is like a normal function except it uses yeild keyword instead
        	of return. the yeild keyword is used whenever the caller function needs a value 
        	and the function containing yeild will retain its local state and continue 
        	executing where it left off after yeilding value to the caller. 

        	Its giving scrapy a generator object. Generators don't hold the entire result in
        	memory, they yeild one result at a time. essentialy generating values as needed.
        	they calculate one result, then forget about it and move one untill the last
        	value. The generator is considered empty once the function runs but does not hit
        	yeild anymore. this can be because the loop has come to a end or it does not 
        	satisfy a if/else statment

	'''


