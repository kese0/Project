from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10) # 묵시적 대기, 활성화를 최대 15초가지 기다린다.

# 페이지 가져오기(이동)
driver.get('https://google.co.kr')

# 5초후 종료
time.sleep(5)
driver.quit() # 웹 브라우저 종료. driver.close()는 탭 종료