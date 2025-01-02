# 셀레니움 기본예제3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.implicitly_wait(15) # 묵시적 대기, 활성화를 최대 15초까지 기다림

# 페이지 가져오기(이동)
driver.get('https://www.google.co.kr')
driver.get('https://www.youtube.com/c/반원')
driver.get('https://www.naver.com')

# 이전 창으로 이동 2번하기
driver.back()
driver.back()

# 다음 창으로 2번 이동하기
driver.forward()
driver.forward()

# 3초 후 종료
time.sleep(3)
driver.quit() # 웹 브라우저 종료. driver.close()는 탭 종료