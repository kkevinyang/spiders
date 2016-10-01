# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from scrapy.spiders import Spider
from scrapy.selector import Selector

from shanbenyoumei.items import ShanbenyoumeiItem

class SBYMSpider(Spider):
    name="shanbenyoumei"

    start_urls=[
        'http://tieba.baidu.com/p/2166231880'
    ]

    def parse(self,response):
        sel=Selector(response)

        image_url=sel.xpath("//div[@id='post_content_29397251028']/img[@class='BDE_Image']/@src").extract()
        print 'the urls:/n'
        print image_url
        print '/n'

        item=ShanbenyoumeiItem()
        item['sbym_image_url']=image_url

        yield item
