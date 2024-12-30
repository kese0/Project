#네이버 주식 사이트 크롤링(select 활용)
import requests
from bs4 import BeautifulSoup

res = requests.get('https://finance.naver.com/sise/')
soup = BeautifulSoup(res.content, 'html.parser')
data = soup.select('.lst_major > li')

for item in data:
    print(item.get_text().strip())