# 셀레니움 기본예제2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome() 
driver.implicitly_wait(15) # 묵시적 대기, 활성화를 최대 15초까지 기다림

# 화면 크기 지정
driver.fullscreen_window() # 전체화면 모드로 변경
time.sleep(1)
driver.maximize_window() # 최대 창 크기로 변경
time.sleep(1)
driver.set_window_rect(100, 100, 500, 500) # 특정 좌표(x, y)와 크기(width,height)로 변경
time.sleep(1)

print(driver.get_window_rect())

# 3초 후 종료
time.sleep(3)
# driver.quit() # 웹 브라우저 종료. driver_close()는 탭 종료
driver.set_window_position(0,0)