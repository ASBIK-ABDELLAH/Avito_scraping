# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AvitoCarsItem(scrapy.Item):
    # define the fields for your item here like:
    car_name = scrapy.Field()
    car_price = scrapy.Field()
    car_city = scrapy.Field()
    car_cv_man_auto = scrapy.Field()
    car_information = scrapy.Field()
    car_equipements = scrapy.Field()


