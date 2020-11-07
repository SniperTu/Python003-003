# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class MovieIpPipeline:
    def open_spider(self, spider):
        self.conn = pymysql.connect(host='127.0.0.1', user='root', password='123456', database='maoyan',port=3306, charset='gbk')
        self.cursor = self.conn.cursor()


    def process_item(self, item, spider):
        movie_name = item['movie_name']
        movie_type = item['movie_type']
        movie_actors = item['movie_actors']
        movie_release_time = item['movie_release_time']

        try:
            self.cur.execute("insert into scrapy(movie_name, movie_type, movie_actors, movie_release_time) values(%s,%s,%s)"\
                             %(movie_name, movie_type, movie_actors, movie_release_time))
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()

        return item
    def close_spider(self, spider):
        self.conn.close()
