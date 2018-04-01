# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XchfutItem(scrapy.Item):
    title_name = scrapy.Field()
    # title_link = scrapy.Field()
    image_link = scrapy.Field()
    # image_path = scrapy.Field()
    publish_data = scrapy.Field()
