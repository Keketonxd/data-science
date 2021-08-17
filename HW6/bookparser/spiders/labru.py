import scrapy
from scrapy.http import HtmlResponse, common
from bookparser.items import JobparserItem


class LabruSpider(scrapy.Spider):
    name = 'labru'
    allowed_domains = ['labirint.ru']
    start_urls = [
        'https://www.labirint.ru/search/фэнтези/?stype=0']

    def parse(self, response: HtmlResponse):
        next_page = response.xpath(
            "//a[@class='pagination-next__text']/@href").extract_first()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

        links = response.xpath(
            "//a[@class='product-title-link']/@href").extract()
        for link in links:
            yield response.follow(link, callback=self.vacancy_parse)

    def vacancy_parse(self, response: HtmlResponse):
        url = response.url
        name = response.xpath(
            "//div[@id='product-title']/h1/text()").extract_first()
        authors = response.xpath(
            "//a[@data-event-label='author']/text()").extract_first()
        common_price = response.xpath(
            "//div[@class='buying-priceold-text']/text()").extract_first()
        sale_price = response.xpath(
            "//div[@class='buying-pricenew-text']/text()").extract_first()
        rating = response.xpath("//div[@id='rate']/text()").extract_first()
        yield JobparserItem(url=url, name=name, authors=authors, common_price=common_price, sale_price=sale_price, rating=rating)
