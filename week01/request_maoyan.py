import logging
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
from time import sleep
from urllib.parse import urljoin

BASE_URL = 'https://trade.maoyan.com/'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
Refer = 'https://trade.maoyan.com/'
header = {'user-agent': user_agent,
          'Refer': Refer}
def get_url_list(url):
    response = requests.get(url, header)
    response.encoding = 'utf-8'
    bs_info = bs(response.text, 'lxml')
    print(response.text)
    urls=[]
    for tags in bs_info.find_all('div', attrs={'class':'movie-item-info'}):
        print(tags)
        for atag in tags.find_all('a'):
            single_url = urljoin(BASE_URL, atag.get('bref'))
            urls.append(single_url)
    return urls

def get_moviesinfo(urls):
    mylist=[]
    header['Refer']='https://maoyan.com/board'
    for url in urls:
        response = requests.get(urls, header)
        bs_info = bs(response.text, 'html.parse')
        movie_name = bs_info.find('h1', attrs={'class': 'name'}).text
        movie_type = ''
        for tags in bs_info.find_all('div', attrs={'class':'movie-brief-container'}):
            for atag in tags.find_all('a'):
                movie_type += atag
        movie_release_time = bs_info.find('div', attrs={'class':'movie-brief-container'}).find_all('li')[-1].text[:10]
        info_list = [movie_name, movie_type,movie_release_time]
        mylist.append(info_list)
        sleep(5)
    return mylist
def save(list):
    data = pd.DataFrame(list)
    data.to_csv('./movie.csv',encoding='gbk',index=False,header=False)
    logging.info('save data to csv')

def main(url):
    urls = get_url_list(url)
    movie_info_lists = get_moviesinfo(urls)
    save(movie_info_lists)

if __name__ == '__main__':
    url = 'https://maoyan.com/board/4'
    main(url)




















