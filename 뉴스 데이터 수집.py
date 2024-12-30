#뉴스 제목과 링크 가져오기
# import requests
# from bs4 import BeautifulSoup

# response = requests.get("https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90")
# html = response.text
# soup = BeautifulSoup(html, 'html.parser')
# links = soup.select(".news_tit") #결과는 리스트로
# for link in links:
#     title = link.text
#     url = link.attrs['href']
#     print(title, url)

# 해당 검색어로 크롤링
# import requests
# from bs4 import BeautifulSoup

# word = str(input('검색어를 입력하세요: '))
# print()
# addr = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query='+word
# response = requests.get(addr)

# html = response.text
# soup = BeautifulSoup(html, 'html.parser')
# links = soup.select(".news_tit") #결과는 리스트로
# for link in links:
#     title = link.text
#     url = link.attrs['href']
#     print(title, url)

# 여러 페이지 결과 모두 가져오기
import requests
from bs4 import BeautifulSoup

word = str(input('검색어를 입력하세요: '))
pages = int(input('원하는 페이지를 입력하세요: '))
print()
pageNum = 1
for i in range(1, pages*10, 10):
    print(f"{pageNum}페이지 입니다.===============================================")
    response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={word}&start={i}")
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.select(".news_tit") #결과는 리스트로
    for link in links:
        title = link.text
        url = link.attrs['href']
        print(title, url)
    print()
    pageNum+=1