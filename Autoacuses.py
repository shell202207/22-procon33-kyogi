# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 20:40:36 2022

@author: ore
"""

#ライブラリ読み込み
from selenium import webdriver
import time
import wave

driver=webdriver.Chrome()

#ページ接続
driver.get('https://procon33-practice.kosen.work/client.html')
time.sleep(1)
#s = input('Enter we token : ')
#10秒終了を待つ
time.sleep(2)
driver.find_element_by_xpath('//*[@id="token"]').send_keys('06f8319a6e272cceec4301599e6d1c604b5c80b7efd1908c8dbf9e45420aba93')
time.sleep(1)

#get match
driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/button').click()
time.sleep(1)
#get problem
driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/button').click()
time.sleep(1)
#get chunk
driver.find_element_by_xpath('/html/body/div/div[5]/div[1]/button').click()
time.sleep(1)

time.sleep(10)
#クロームの終了処理
#driver.close()
