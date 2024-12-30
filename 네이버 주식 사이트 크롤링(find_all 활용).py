#네이버 주식 사이트 크롤링(find_all 활용)
import requests
from bs4 import BeautifulSoup

res = requests.get('https://finance.naver.com/sise/')
soup = BeautifulSoup(res.content, 'html.parser')
ul_element = soup.find('ul', class_='lst_major')
data = ul_element.find_all('li')

for item in data:
    print(item.get_text().strip())