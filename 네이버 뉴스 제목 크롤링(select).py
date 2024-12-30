# 네이버 뉴스 제목 크롤링(select 활용)
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://search.naver.com/search.naver?ssc=tab.news.all&where=news&sm=tab_jum&query=%EB%AF%B8%EC%88%A0+%EA%B2%BD%EB%A7%A4"
html = urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
html_class = soup.select('.news_tit')

for tit in html_class:
    title = tit.text.strip()
    print(title)