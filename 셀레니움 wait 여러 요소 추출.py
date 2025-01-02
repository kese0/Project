from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome(service=Service(ChromeDriverManager().install())) as driver:
    driver.get("https://indistreet.com/live?sortOption=startDate%3AASC")
    driver.implicitly_wait(10)
    #그리드 형태에서는 view 하나 안에 있는 구조는 똑같음. 그리드의 몇 번째 요소냐만 달라진다.
    for i in range(1, 11):  #총 10 개의 공연 제목을 스크래핑 하기 위한 반복문
        element = driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div[4]/div[1]/div[{}]/div/a/div[2]/p[1]'.format(i))
        print(element.text)