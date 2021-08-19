import scrapy
from scrapy.http import HtmlResponse
from leruaparser.items import LeruaparserItem
from scrapy.loader import ItemLoader


class LeruaSpider(scrapy.Spider):
    name = 'leroy'
    allowed_domains = ['leroymerlin.ru']

    def __init__(self, search):
        super(LeruaSpider, self).__init__()
        self.start_urls = [f'https://leroymerlin.ru/search/?q={search}&suggest=true']

    def parse(self, response: HtmlResponse):
        next_page = response.xpath(
            "//a[@data-qa-pagination-item='right']/@href").extract_first()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
        links = response.xpath("//a[@data-qa='product-image']/@href").extract()
        for link in links:
            yield response.follow(link, callback=self.parse_ads)

    def parse_ads(self, response: HtmlResponse):
        loader = ItemLoader(item=LeruaparserItem(), response=response)
        loader.add_xpath("name", "//h1/text()")
        loader.add_xpath(
            "photos", "//source[@media=' only screen and (min-width: 1024px)']/@srcset")
        loader.add_xpath("character", "//div[@class = 'def-list__group']/text()")
        loader.add_xpath("price", "//span[@slot='price']/text()")
        loader.add_value("url", response.url)

        yield loader.load_item()
