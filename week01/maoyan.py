import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
cookie ='__mta=222132903.1598194177096.1598194244476.1598194249687.5; uuid_n_v=v1; uuid=DC8C70F0E54F11EA92FADB0AB124FC3BB977B1F4B1774875BD0D43B7DAE66485; _csrf=55ff3b8433dce9676614856deaa19cdee43f28847285e36a8f98f7cc4cbf18d0; _lxsdk_cuid=1741bcbd170c8-05e48657414c2b-3323766-144000-1741bcbd170c8; _lxsdk=DC8C70F0E54F11EA92FADB0AB124FC3BB977B1F4B1774875BD0D43B7DAE66485; mojo-uuid=7fbff91a522dc7ff56c4c26802c3c63e; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1598194176,1598194244,1598195146; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1598195146; __mta=222132903.1598194177096.1598194249687.1598195146187.6; _lxsdk_s=1741c0585e6-ed9-12a-1bf%7C%7C1'

header = {
    'user-agent': user_agent,
    'Cookie': cookie
    }

url = "https://maoyan.com/films?showType=3"
response = requests.get(url,headers=header)
bs_info = bs(response.text, 'html.parser')

result = []
for tag in bs_info.find_all('div', attrs={'class': 'movie-hover-info'}, limit=10):
    # 电影名称
    name = tag.find('span', attrs={'class': 'name'}).text
    # 电影类型
    category = tag.find('span', text='类型:').parent.text.split('\n')[-2].strip()
    # 上映时间
    show_time = tag.find('span', text='上映时间:').parent.text.split('\n')[-2].strip()

    result.append(tuple([name, category, show_time]))

movie1 = pd.DataFrame(data = result)
movie1.to_csv('./猫眼电影.csv', encoding='utf8')
