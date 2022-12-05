# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WorldometersItem(scrapy.Item):
    names=scrapy.Field()
    year=scrapy.Field()
    population=scrapy.Field()
   
