import time
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd


def chrome(headless=False):
    # support to get response status and headers
    d = webdriver.DesiredCapabilities.CHROME
    d['loggingPrefs'] = {'performance': 'ALL'}
    opt = webdriver.ChromeOptions()
    if headless:
        opt.add_argument("--headless")
    opt.add_experimental_option('excludeSwitches', ['enable-logging'])
    opt.add_argument("--disable-popup-blocking")
    browser = webdriver.Chrome(executable_path=r'driver/chromedriver.exe', options=opt,desired_capabilities=d)
    browser.implicitly_wait(10)
    return browser
## Pass True if you want to hide chrome browser
browser = chrome(False)
browser.get('https://www.linkedin.com/uas/login')
browser.implicitly_wait(3)
file = open('config.txt')
lines = file.readlines()
username = lines[0]
password = lines[1]


elementID = browser.find_element_by_id('username')
elementID.send_keys(username)

elementID = browser.find_element_by_id('password')
elementID.send_keys(password)

browser.get('https://www.linkedin.com/search/results/companies/?companyHqGeo=%5B%22102221843%22%5D&origin=FACETED_SEARCH&sid=3LH')



src = browser.page_source
soup = BeautifulSoup(src, 'lxml')

#a = browser.find_element_by_xpath(f"/html/body/div[6]/div[3]/div/div[2]/div/div[1]/main/div/div/div[1]/ul/li[1]/div/div/div[2]/div[1]/div[1]/div/span/span/a").t
first = soup.find('div', {'Xpath': '/html/body/div[6]/div[3]/div/div[2]/div/div[1]/main/div/div/div[1]/ul/li[1]/div/div/div[2]/div[1]/div[1]/div/span/span/a'}).get_text().strip()
print(first)