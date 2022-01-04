from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import selenium.common.exceptions as sel_exceptions


class Chrome(object):
    # 페이지 이동 할 때 로딩을 위해 기다리는 시간. 기다리는 시간을 수동으로 입력하는 implicity wait 방식을 취했으나,
    # 필요할 경우 explicity wait 방식을 찾아서 이용할 것.
    wait_sec = 5

    def __init__(self):
        path = './chromedriver/chromedriver_96.exe'
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        # chrome_options.add_argument('add_argument("disable-gpu")')
        # chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko")
        self.driver = webdriver.Chrome(os.path.abspath(path), chrome_options=chrome_options)

    def move(self, url):
        print(f'move to {url}!')
        self.driver.get(url)
        self.driver.implicitly_wait(self.wait_sec)

    def move_back(self):
        print(f'move before page!')
        self.driver.back()
        self.driver.implicitly_wait(self.wait_sec)

    # xpath를 입력받아서 클릭함.
    def click_by_xpath(self, xpath):
        # print(f'click: {xpath}')
        try:
            self.driver.find_element_by_xpath(xpath).click()
        except sel_exceptions.ElementNotInteractableException:
            self.driver.find_element_by_xpath(xpath).send_keys(Keys.ENTER)
        except sel_exceptions.ElementClickInterceptedException:
            element = self.driver.find_element_by_xpath(xpath)
            self.driver.execute_script('arguments[0].click();', element)
        except sel_exceptions.NoSuchElementException:
            print('No such element!!')
            return
        self.driver.implicitly_wait(self.wait_sec)
        print(f'click {self.driver.current_url}')
        return

    # xpath의 href 속성을 가져오는데, 주로 url을 가져올 때 쓰임
    def get_url(self, xpath):
        # print(xpath)
        try:
            u = self.driver.find_element_by_xpath(xpath).get_attribute('href')
            return u
        except sel_exceptions.NoSuchElementException:
            # print('No such element!!')
            return 'NSE'


# # xpath 의 최하위 태그의 인덱스만 다른 xpath 의 개수를 리턴. ex) ul/li[1] ~ ul/li[4] 까지 존재하면 4를 리턴
# def count_these_xpath(self, xpath):
#     xpath = re.compile('\\[\\d+\\]$').sub('', xpath)
#     num = len(self.driver.find_elements_by_xpath(xpath))
#     return num