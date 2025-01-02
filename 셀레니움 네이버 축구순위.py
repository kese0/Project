from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

driver = webdriver.Chrome()

# 결과를 저장할 빈 DataFrame을 생성
df_bundes_team = pd.DataFrame(columns=['rank', 'team', 'game', 'win_pt', 'win', 'draw', 
                                         'lose', 'gf', 'ga', 'goal_diff'])

# Bundesliga 순위 페이지 URL
bundes_football = "https://sports.news.naver.com/wfootball/record/index?category=bundesliga&tab=team"
driver.get(bundes_football)

# 명시적 대기 사용
try:
    # 페이지가 로드되는데 충분한 시간을 기다리기 위해 추가적으로 time.sleep()을 사용
    time.sleep(5)  # 5초 대기 (동적 콘텐츠 로딩을 기다리는 시간)
    
    # 테이블이 로드될 때까지 기다림
    WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '#wfootballTeamRecordBody > table > tbody > tr'))
    )
    
    # tr_elements 로 모든 행을 가져옴
    tr_elements = driver.find_elements(By.CSS_SELECTOR, '#wfootballTeamRecordBody > table > tbody > tr')

    # 각 행을 순차적으로 처리
    for i in range(1, len(tr_elements) + 1):
        try:
            rank = driver.find_element(By.CSS_SELECTOR, f'#wfootballTeamRecordBody > table > tbody > tr:nth-child({i}) > td:nth-child(1) > div > strong').text
            team = driver.find_element(By.CSS_SELECTOR, f'#wfootballTeamRecordBody > table > tbody > tr:nth-child({i}) > td:nth-child(2) > div > span.name').text
            game = driver.find_element(By.CSS_SELECTOR, f'#wfootballTeamRecordBody > table > tbody > tr:nth-child({i}) > td:nth-child(3) > div > span').text
            win_pt = driver.find_element(By.CSS_SELECTOR, f'#wfootballTeamRecordBody > table > tbody > tr:nth-child({i}) > td:nth-child(4) > div > span').text
            win = driver.find_element(By.CSS_SELECTOR, f'#wfootballTeamRecordBody > table > tbody > tr:nth-child({i}) > td:nth-child(5) > div > span').text
            draw = driver.find_element(By.CSS_SELECTOR, f'#wfootballTeamRecordBody > table > tbody > tr:nth-child({i}) > td:nth-child(6) > div > span').text
            lose = driver.find_element(By.CSS_SELECTOR, f'#wfootballTeamRecordBody > table > tbody > tr:nth-child({i}) > td:nth-child(7) > div > span').text
            gf = driver.find_element(By.CSS_SELECTOR, f'#wfootballTeamRecordBody > table > tbody > tr:nth-child({i}) > td:nth-child(8) > div > span').text
            ga = driver.find_element(By.CSS_SELECTOR, f'#wfootballTeamRecordBody > table > tbody > tr:nth-child({i}) > td:nth-child(9) > div > span').text
            goal_diff = driver.find_element(By.CSS_SELECTOR, f'#wfootballTeamRecordBody > table > tbody > tr:nth-child({i}) > td:nth-child(10) > div > span').text

            # 각 행을 DataFrame에 추가
            df_bundes_team = df_bundes_team.append({'rank': rank, 'team': team, 'game': game, 'win_pt': win_pt, 'win': win, 'draw': draw, 
                                                     'lose': lose, 'gf': gf, 'ga': ga, 'goal_diff': goal_diff}, ignore_index=True)

        except Exception as e:
            print(f"Error occurred at row {i}: {e}")

except Exception as e:
    print(f"Error loading the page: {e}")

# 결과 출력
print(df_bundes_team, '\n')

# 드라이버 종료
driver.quit()