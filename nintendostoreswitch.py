# -*- coding: utf-8 -*-
import sys
import lxml.html
import time
import webbrowser
from selenium import webdriver
from datetime import datetime
from ctypes import *

print("start " + datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
target_url = 'https://store.nintendo.co.jp/customize.html'
driver = webdriver.PhantomJS()
driver.get(target_url)
root = lxml.html.fromstring(driver.page_source)

result = "SOLD OUT"
i = 0

while result == "SOLD OUT":
    time.sleep(2)
    result = "エラー"
    i = 0
    while result == "エラー":
        i = i + 1
        driver.get(target_url)
        root = lxml.html.fromstring(driver.page_source)
        result = root.cssselect('title')[0].text
    result = root.cssselect('.stock')[0].text
    if i > 1:
        print(result + " " + datetime.now().strftime("%Y/%m/%d %H:%M:%S") + " " + str(i))
    
print(result + " " + datetime.now().strftime("%Y/%m/%d %H:%M:%S") + " " + str(i))
webbrowser.open(target_url)
user32 = windll.user32
user32.MessageBoxA(0,result,time,0)
driver.quit()
sys.exit()
