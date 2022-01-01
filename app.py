
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

cardInfo = findCard('309-AAA') #傳入卡號 取回卡片效果（str格式）
print(cardInfo)
