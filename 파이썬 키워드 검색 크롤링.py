#"파이썬"이라는 키워드 검색 크롤링

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# WebDriver 시작
driver = webdriver.Chrome()

# Google 접속
driver.get('https://www.google.com')

# 검색창 찾기
search_box = driver.find_element(By.NAME, 'q')

# 검색어 입력
search_box.send_keys('파이썬')

# 검색 실행
search_box.send_keys(Keys.RETURN)

# 결과를 확인할 수 있도록 몇 초 대기
time.sleep(5)