# -*- coding: utf-8 -*-
import sys
import lxml.html
from selenium import webdriver
from datetime import datetime
from ctypes import *

time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")

target_url = 'https://store.nintendo.co.jp/customize.html'
driver = webdriver.PhantomJS()
driver.get(target_url)
root = lxml.html.fromstring(driver.page_source)
driver.quit()

result = root.cssselect('title')[0].text
if result == "エラー":
    print(result +" " + time)
    sys.exit()

result = root.cssselect('.stock')[0].text
if result == "SOLD OUT":
    print(result +" " + time)
    sys.exit()

print(result +" " + time)
user32 = windll.user32
user32.MessageBoxA(0,result,time,0)
sys.exit()
