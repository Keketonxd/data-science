from lxml import html
import requests
from pymongo import MongoClient


link = 'https://news.mail.ru/'
response = requests.get(link)
dom = html.fromstring(response.text)
pictured_news = dom.xpath("//div[contains(@class, 'daynews__item')]")

client = MongoClient('127.0.0.1', 27017)
db = client['news_collection']
news = db.news
info = {}


def all_info_after_src(list_of_links):
    for href in list_of_links:
        response = requests.get(href)
        news_dom = html.fromstring(response.text)
        source = news_dom.xpath(
            "//a[contains(@class, 'breadcrumbs__link')]/span/text()")
        date = news_dom.xpath("//span[contains(@class, 'js-ago')]/@datetime")

    info['source'] = source
    info['name'] = name
    info['news_link'] = news_link
    info['date'] = date

    news.update_many({'news_link': info['news_link']}, {
        '$set': info}, upsert=True)


for picture in pictured_news:

    news_link = picture.xpath(
        ".//a[contains(@class, 'js-topnews__item')]/@href")
    name = picture.xpath(".//span[contains(@class, 'photo__title')]/text()")
    all_info_after_src(news_link)


# если убрать ограничения на ul, то можно собрать вообще все новости со странички кроме областных
unpictured_news = dom.xpath(
    "//ul[contains(@class, 'js-module')]/li[@class='list__item']")
for el in unpictured_news:
    news_link = el.xpath(
        ".//a/@href")
    name = el.xpath(".//a/text()")
    all_info_after_src(news_link)
