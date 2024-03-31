# import feedparser
# import webbrowser
from urllib.request import urlopen
from bs4 import BeautifulSoup


# Daum 뉴스 RSS 피드 URL
url = urlopen("http://media.daum.net")

# 웹 페이지 가져오기
response = BeautifulSoup(url, "html.parser")

# 리스트에 있는 뉴스 헤드라인을 라벨에 출력
for link in response.find_all('a'):
    print(link.text.strip(), link.get('herf'))

for link in response.find_all('img'):
    print(link.text.strip(), link.get('src'))