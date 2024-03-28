import requests
from bs4 import BeautifulSoup

# 네이버 실시간 검색어 페이지 URL
url = 'https://www.naver.com'

# 웹 페이지 가져오기
response = requests.get(url)

# HTML 파싱
soup = BeautifulSoup(response.text, 'html.parser')

# 실시간 검색어 순위 추출
for rank, keyword in enumerate(soup.select('.PM_CL_realtimeKeyword_rolling span[class*=ah_k]'), 1):
    print(f'{rank}위: {keyword.get_text()}')
