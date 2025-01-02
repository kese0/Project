from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# 10초 동안 Implicit Wait를 진행하도록 한 후 스크래핑 

#with-as절을 통해 명령어가 끝나면 자체적으로 driver 객체를 소멸시켜 준다.
with webdriver.Chrome(service=Service(ChromeDriverManager().install())) as driver: 
    driver.get("https://indistreet.com/live?sortOption=startDate%3AASC")
    
    #요청이 완벽하게 응답이 되면 다음을 실행하거나 10초를 기다린다. -> 10초까지를 기다리는데 렌더링이 끝나면 그때 종료
    driver.implicitly_wait(10)  
    print(driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div[4]/div[1]/div[1]/div/a/div[2]/p[1]').text)