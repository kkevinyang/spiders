# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ShanbenyoumeiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    sbym_image_url = scrapy.Field()
    images = scrapy.Field()
