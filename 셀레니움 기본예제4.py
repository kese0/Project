# 셀레니움 기본예제4
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.implicitly_wait(15)

# 페이지 가져오기(이동)
driver.get('https://www.naver.com')

# 요소 찾기 - 검색창 찾고 키 전송
search = driver.find_element('css selector', '#query')
search.send_keys('고슴도치')
search.send_keys(Keys.ENTER)
time.sleep(2)

# 요소 찾기 - 지식백과에서 고슴도치 클릭
posts = driver.find_elements('css selector', 'a.tit')
posts[0].click()
time.sleep(2)