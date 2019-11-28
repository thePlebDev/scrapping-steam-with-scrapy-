# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Product(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    

    '''
    - using this class to declare a scrapy item. Normaly scrapy returns extracted data as a 
    python dictionary. however, it is wasy to mess up with a dic exspecialy in larger projects
    The item class provides a simple container used to collect the scraped data. They provide
    dictionary-like API with a convenient syntax for declaring their available fields
    - exporters look at declared fields to figure out columns to export 
    '''
