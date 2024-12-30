# 네이버 뉴스 제목 크롤링(find_all 활용)
from urllib.request import urlopen
from bs4 import BeautifulSoup

# 뉴스기사 검색 URL -> NAVER에 미술 경매 검색 후 뉴스 탭으로 이동한 뒤 복사한 URL
url = "https://search.naver.com/search.naver?ssc=tab.news.all&where=news&sm=tab_jum&query=%EB%AF%B8%EC%88%A0+%EA%B2%BD%EB%A7%A4"

# urlopen 함수를 통해 url 주소를 open 하여 읽고, 그 값을 html 이라는 변수에 저장
html = urlopen(url).read()

# html 정보가 담겨있는 변수를 bs4 라이브러리에 있는 BeautifulSoup를 이용
# Parsing하여 soup에 저장
soup = BeautifulSoup(html, 'html.parser')

# parsing된 결과인 soup에서 news_tit class(뉴스 제목 클래스 의미)를 검색하고, 모든 정보 찾기
html_class = soup.find_all(class_='news_tit')

# print(html_class)

# 뉴스제목을 text로 추출하여 출력
for tit in html_class:
    title = tit.text.strip()
    print(title)