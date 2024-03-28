import requests
from bs4 import BeautifulSoup

# 네이버 실시간 검색어 페이지 URL
url = 'https://www.naver.com'

# 웹 페이지 가져오기
response = requests.get(url)

# HTML 파싱
soup = BeautifulSoup(response.text, 'html.parser')

# 실시간 검색어가 있는 부분의 HTML 태그와 클래스를 확인하여 찾기
realtime_search = soup.find('ol', class_='lst_realtime_srch')

# 검색어를 가져와 출력
if realtime_search:
    print("네이버 실시간 검색어 순위:")
    # 실시간 검색어 순위 추출
    for rank, keyword in enumerate(soup.select('.PM_CL_realtimeKeyword_rolling span[class*=ah_k]'), 1):
        print(f'{rank}위: {keyword.get_text()}')
else:
    print("실시간 검색어를 찾을 수 없습니다.")