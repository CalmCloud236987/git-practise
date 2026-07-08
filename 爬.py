from fake_useragent import UserAgent
from  bs4 import BeautifulSoup
import requests
import time
import random

ua = UserAgent()
headers = {'User-Agent':ua.random}

for page in range(3):
    start = page*25
    url = f'https://movie.douban.com/top250?start={start}'
    time.sleep(random.uniform(5,10))
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text,"html.parser")
    items = soup.find_all('div',class_='item')
    for item in items:
        rank = item.find('em').text
        try:
            title = item.find('span',class_='title').text
        except:
            title = "无标题"
        rating = item.find('span',class_='rating_num').text

        print(f"排名：{rank}|{title}|评分：{rating}")
    print(f"---第{page+1}页完成---\n")
    

