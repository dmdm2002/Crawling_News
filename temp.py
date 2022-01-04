from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import quote
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import math

pageCount = math.ceil(10 / 10)
print(pageCount)
# url = 'https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query='
#
# keyworld = '펜싱'
# query = quote(keyworld)
# news_url = f'{url}{query}'
#
# path = './chromedriver/chromedriver_96.exe'
# chrome_options = webdriver.ChromeOptions()
# # chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')
# # chrome_options.add_argument('add_argument("disable-gpu")')
# # chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko")
# driver = webdriver.Chrome(os.path.abspath(path), chrome_options=chrome_options)
#
# page_path = '&sort=1&photo=0&field=0&pd=0&ds=&de=&cluster_rank=77&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start=1'
# driver.get(news_url)
# driver.implicitly_wait(20)
# driver.get(f'{news_url}{page_path}')
# driver.implicitly_wait(20)
# print(driver.page_source)

# # news_url = f'{url}{query}'
# # html = urlopen(news_url)
# # data = html.read().decode('utf8')
# soup = BeautifulSoup(driver.page_source, 'lxml')
#
# datas = soup.select('#main_pack > section > div > div.group_news > ul > li > div > div > a')
#
# get_item_count = 5
#
# # url_list = []
# # for i in range(get_item_count):
# #     temp = datas[i]
# #     url_list.append(f"{temp.get('href')}")
#
# print(len(datas))
# print(datas[0].get('href'))
# print(datas[0].text.strip())
# news_list_html = soup.find_all('ul', class_='list_news')
# print(news_list_html)