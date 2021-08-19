# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import scrapy
from itemadapter import ItemAdapter
from pymongo import MongoClient
from scrapy.pipelines.images import ImagesPipeline


class LeruaparserPipeline:
    def process_item(self, item, spider):
        if isinstance(item, str):
            item['price'] = float(item['price'])
        if isinstance(item, list):
            item['price'] = [float(price) for price in item['price']]
        collection = self.mongo_base[spider.name]
        collection.insert_one(item)
        return item


class LeruaPhotosPipeline(ImagesPipeline):
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongo_base = client['books']

    def get_media_requests(self, item, info):
        if item['photos']:
            for img in item['photos']:
                try:
                    yield scrapy.Request(img)
                except Exception as e:
                    print(e)

    def item_completed(self, results, item, info):
        if results:
            item['photos'] = [itm[1] for itm in results if itm[0]]
        return item
