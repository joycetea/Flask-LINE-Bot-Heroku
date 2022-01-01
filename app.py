from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup


def findCard(cardID : str) -> str: 
    #cardID = '309-007' #之後代換LINE OCR內容
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("--disable-notifications")
    ser=Service(ChromeDriverManager().install())
    chrome = webdriver.Chrome(service=ser, options=options)
    chrome.get("http://220.134.173.17/gameking/card/ocg_show.asp?call_no=" + cardID)
     
    strR = ""
    try:
        soup = BeautifulSoup(chrome.page_source, 'html.parser')
        card_query = soup.select('p table')[1].select('tbody tr td')
        strR += card_query[1].text + '\n'
        result = strR
        
    except Exception as ex:
        result = '查無此卡'
        
    if result == '' or result is None:
         result = '查無此卡'
    return result

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 20:03:37 2021

@author: eugenetseng
"""

from FindCard import findCard

cardInfo = findCard('309-AAA') #傳入卡號 取回卡片效果（str格式）
print(cardInfo)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By


PATH = "./chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.db.yugioh-card.com/yugiohdb/deck_search.action?request_locale=ja")
search = driver.find_element_by_name("cardname")
search.send_keys("マジクリボー") #之後用OCR掃出來的卡名取代這裡的マジクリボー
search.send_keys(Keys.RETURN)

time.sleep(5)

links = driver.find_elements(By.TAG_NAME, "a")

count = 0
while count <=29:
    del links[0]
    count = count+1

addrs = [0,1,2,3,4]
count = 0
while count <= 4:
    addrs.insert(count,links[0])
    del links[0]
    count = count+1
    
for addr in addrs:
    print (addr.get_attribute("href"))
#addrs是一個list，裡面存了最新分享的五個牌組的網址
time.sleep(5)
driver.quit()
