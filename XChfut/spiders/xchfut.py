# -*- coding: utf-8 -*-
import scrapy
from XChfut.items import XchfutItem

class XchfutSpider(scrapy.Spider):
    name = 'xchfut'
    allowed_domains = ['xc.hfut.edu.cn']
    # start_urls = ['http://xc.hfut.edu.cn/120/list']
    baseURL = 'http://xc.hfut.edu.cn/120/list'
    offset = 1
    start_urls = [baseURL + str(offset) + '.htm']
    print(start_urls)

    def parse(self, response):
        # print(response.body.decode('utf-8'))
        url_list = response.xpath('//a[@class=" articlelist1_a_title "]')
        # print(url_list)
        for url in url_list:
            # print(url.xpath('./@href').extract()[0])
            if 'news.hfut.edu.cn' not in url.xpath('./@href').extract()[0]:
                # print('http://xc.hfut.edu.cn/' + url.xpath('./@href').extract()[0])
                yield scrapy.Request('http://xc.hfut.edu.cn/' + url.xpath('./@href').extract()[0]
                                     ,callback=self.parse_image)

        # print(response.xpath('//a[@title="进入下一页"]/@disabled').extract())

        if response.xpath('//a[@title="进入下一页"]/@disabled').extract() != ['disabled']:
            self.offset += 1
            yield scrapy.Request(self.baseURL + str(self.offset) + '.htm',callback=self.parse)
        else:return

    def parse_image(self,response):
        item = XchfutItem()
        # print(response.body.decode('utf-8'))
        item['title_name'] = response.xpath('//h1[@class="atitle"]/text()').extract()[0].strip()
        item['publish_data'] = response.xpath('//span[@class="posttime"]/text()').extract()[0][5:]
        # print(item)
        image_links = response.xpath('//p/img/@src | //span/img/@src').extract()
        # print(image_links)
        item['image_link'] = []
        for image_link in image_links:
            if '.jpg' in image_link or '.png' in image_link:
                item['image_link'].append('http://xc.hfut.edu.cn'+image_link)
        yield item
        # print(item)



