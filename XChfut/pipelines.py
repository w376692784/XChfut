# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
import scrapy
import os
from XChfut.settings import IMAGES_STORE as image_store

class XchfutPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        image_links = item['image_link']
        for image_link in image_links:
            # image_link = image_link.decode('utf-8')
            yield scrapy.Request(image_link)

    def item_completed(self, results, item, info):
        # print(results)
        image_paths = [x['path'] for sym,x in results if sym]
        # print(image_paths)\
        if not os.path.exists(image_store + item['title_name']):
            os.mkdir(image_store + item['publish_data']+' '+item['title_name'])
        i = 1
        for image_path in image_paths:
            # print(image_store + image_path)
            os.rename(image_store + image_path, image_store + item['publish_data'] + ' ' + item['title_name'] + '/'
                      + item['title_name'] + str(i) + '.jpg')
