import scrapy
from scrapy import Selector
from movie_ip.items import MovieIpItem

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def parse(self, response):
        selector = Selector(response=response)
        print(response.text)
        movie_list = selector.xpath('//div[@class="movie-honer-info"]')
        for movie_info in movie_list:
            attr_list = movie_info.xpath('./div')
            movie_name = attr_list[0].xpath('./@title').extract_first().strip()
            movie_type = attr_list[1].xpath('./@text()').extract()[1].strip()
            movie_actors = attr_list[2].xpath('./text()').extract()[1].strip()
            movie_release_time = attr_list[3].xpath('./text()').extract()[1].strip()

            item = MovieIpItem()
            item['movie_name'] = movie_name
            item['movie_type'] = movie_type
            item['movie_actors'] = movie_actors
            item['movie_release_time'] = movie_release_time
            yield item