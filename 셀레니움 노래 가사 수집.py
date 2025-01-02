# Melon에서 노래 가사 수집하는 셀레니움 크롤링 예제

# 크롤링 기본 라이브러리 import
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import time
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# 드라이버 실행
driver = webdriver.Chrome()
# 웹주소 입력
url = 'https://www.melon.com/index.htm'
driver.get(url)
# 창 크기를 최대화
driver.maximize_window()
#검색창 찾기
elem = driver.find_element(By.ID, "top_search")
elem.clear()
# 검색어 입력
elem.send_keys('재쓰비 너와의 모든 지금')
time.sleep(1)
# 엔터키 입력
elem.send_keys(Keys.RETURN)
# '앨범' 메뉴을 xpath로 찾아 클릭 //*[@id="divCollection"]/ul/li[4]/a/span
album = driver.find_element(By.XPATH, '//*[@id="divCollection"]/ul/li[4]/a/span')
album.click()
#앨범 이미지를 xpath 찾아 클릭 //*[@id="frm"]/div/ul/li/div/a[1]/span
driver.find_element(By.XPATH, '//*[@id="frm"]/div/ul/li/div/a[1]/span').click()
# 가사 아이콘 찾아서 클릭 -XPATH로 찾기 '//*[@id="frm"]/div/table/tbody/tr[2]/td[3]/div/a'
driver.find_element(By.XPATH, '//*[@id="frm"]/div/table/tbody/tr/td[3]/div/a').click()
# id로 가사가 있는 요소를 찾아 .text로 가사만 가져와서 프린트
lyric = driver.find_element(By.ID, 'd_video_summary').text
print(lyric)