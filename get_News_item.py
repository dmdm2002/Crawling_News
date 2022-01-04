import re

from Settings import options
from bs4 import BeautifulSoup
from urllib.parse import quote
from selenium import webdriver
import os
import math
import re

class Crawling_news(options):
    def __init__(self, keywork, get_item_count):
        super(Crawling_news, self).__init__()
        self.keyword = keywork
        self.get_item_count = get_item_count
        self.query = quote(self.keyword)
        self.driver = webdriver.Chrome(os.path.abspath(self.driver_path), chrome_options=self.chrome_options)

    def get_item(self):
        pages = math.ceil(self.get_item_count / 10)

        url_list = []
        name_list = []

        stack_count = 0
        try:
            for now_page in range(pages):
                if now_page == 0:
                    news_url = f'{self.root_url}{self.query}{self.add_url}1'
                else:
                    news_url = f'{self.root_url}{self.query}{self.add_url}{now_page}1'
                    print(news_url)

                self.driver.get(news_url)
                self.driver.implicitly_wait(5)
                soup = BeautifulSoup(self.driver.page_source, 'lxml')
                datas = soup.select('#main_pack > section > div > div.group_news > ul > li > div > div > a')

                if now_page == pages-1:
                    for i in range(self.get_item_count - stack_count):
                        temp = datas[i].text.strip()
                        indx = temp.find(self.keyword)
                        if indx != -1:
                            url_list.append(datas[i].get('href'))
                            name_list.append(datas[i].text.strip())
                else:
                    for i in range(len(datas)):
                        temp = datas[i].text.strip()
                        indx = temp.find(self.keyword)
                        if indx != -1:
                            url_list.append(datas[i].get('href'))
                            name_list.append(datas[i].text.strip())

                stack_count = stack_count + 10

            self.driver.close()

        except:
            self.driver.close()

        return url_list, name_list