# -*- coding: utf-8 -*-
import sys
import lxml.html
import time
import webbrowser
from selenium import webdriver
from datetime import datetime
driver = webdriver.PhantomJS()
i = 0
j = 0
target_url = 'https://store.nintendo.co.jp/customize.html'

print("start " + datetime.now().strftime("%Y/%m/%d %H:%M:%S"))

result = "SOLD OUT"
while result == "SOLD OUT":
    nowtime = datetime.now().strftime("%H:%M:%S") 
    time.sleep(3)
    result = "エラー"
    i = 0
    j = j + 1
    while result == "エラー":
        i = i + 1
        driver.get(target_url)
        root = lxml.html.fromstring(driver.page_source)
        result = root.cssselect('title')[0].text
        if i > 100:
            print("エラー " + nowtime + " - " + datetime.now().strftime("%H:%M:%S")+ " " + i)
            time.sleep(300)
    result = root.cssselect('.stock')[0].text
    if i > 1:
        print(result + " " + str(nowtime) + " - " + datetime.now().strftime("%H:%M:%S") + " エラー" + str(i))
    if j % 100 == 0 :
        print("SOLD OUT " + str(j) + " " + str(nowtime))

print(result + " " + datetime.now().strftime("%Y/%m/%d %H:%M:%S") + " " + str(i))
webbrowser.open(target_url)
driver.quit()
sys.exit()