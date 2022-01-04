from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyperclip

sleep_sec = 3


def naver_login(title, news_url):
    driver = webdriver.Chrome('./chromedriver/chromedriver_96.exe')

    url = 'https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com'
    uid = 'rlawjdtn98'
    upw = 'vnttkrhk15'

    driver.get(url)
    time.sleep(sleep_sec)

    tag_id = driver.find_element_by_name('id')
    tag_pw = driver.find_element_by_name('pw')

    tag_id.click()
    pyperclip.copy(uid)
    tag_id.send_keys(Keys.CONTROL, 'v')
    time.sleep(sleep_sec)

    tag_pw.click()
    pyperclip.copy(upw)
    tag_pw.send_keys(Keys.CONTROL, 'v')
    time.sleep(sleep_sec)

    login_btn = driver.find_element_by_id('log.login')
    login_btn.click()
    time.sleep(sleep_sec)

    driver.get('https://cafe.naver.com/fencers')
    time.sleep(sleep_sec)

    news_page = driver.find_element_by_xpath('//*[@id="menuLink69"]')
    news_page.click()
    time.sleep(sleep_sec)

    write_page = driver.find_element_by_xpath('//*[@id="cafe-info-data"]/div[3]/a')
    write_page.click()
    time.sleep(sleep_sec)

    driver.switch_to.frame(driver.find_element_by_id("cafe_main"))

    name = driver.find_element_by_id("subject")
    name.click()
    pyperclip.copy(title)
    name.send_keys(Keys.CONTROL, 'v')
    time.sleep(sleep_sec)

    writing = driver.find_element_by_id("textbox")
    writing.click()
    pyperclip.copy(news_url)
    writing.send_keys(Keys.CONTROL, 'v')
    time.sleep(sleep_sec)

    complete = driver.find_element_by_xpath('//*[@id="app"]/div/div/section/div/div[1]/div/a')
    complete.click()
    time.sleep(sleep_sec)


naver_login('a', 'b')