import scrapy
from scrapy import Selector
from maoyanspider.items import MaoyanspiderItem

BASE_URL = 'https://maoyan.com'
class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/films']

    def start_requests(self):
        yield scrapy.Request(url=f'https://maoyan.com/films', callback=self.parse())

    def parse(self, response):
        tags = Selector(response=response).xpath('//div[@class="channel-detail movie-item-title"]')[:10]
        for tag in tags:
            url=BASE_URL+tag.xpath('./a/@hbref').extract_first()
            yield scrapy.Request(url=url, callback=self.parse2)
    def parse2(self, response):
        item = MaoyanspiderItem()
        movie_brief = Selector(response=response).xpath('//div[@class="movie_brief-container"]')
        name = movie_brief.xpath('./h1/text()').extract()
        categories = movie_brief.xpath('./ul/li/a').extract()
        published_at=movie_brief.xpath('./ul/li[last()]/text()').extract()

        item['name']=name
        item['categories']=[category.strip() for category in categories]
        item['published-at']=published_at

        yield item


















