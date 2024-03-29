import requests
from bs4 import BeautifulSoup
import tkinter as tk

def scrape_and_display():
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
        # 검색어 리스트 초기화
        search_terms = []
        print("네이버 실시간 검색어 순위:")
        # 각 검색어를 리스트에 추가
        for item in realtime_search.find_all('span', class_='ah_k'):
            search_terms.append(item.text)
        
        # 리스트에 있는 검색어를 라벨에 출력
        for idx, term in enumerate(search_terms):
            label = tk.Label(root, text=f"{idx + 1}. {term}")
            label.pack()
    else:
        label = tk.label(root, text="실시간 검색어를 찾을 수 없습니다.")
        label.pack()

# Tkinter 윈도우 생성
root = tk.Tk()
root.title("네이버 실시간 검색어")

# 스크래핑 및 화면 출력 버튼 생성
scrape_button = tk.Button(root, text="실시간 검색어 가져오기", command=scrape_and_display)
scrape_button.pack()

# 윈도우 실행
root.mainloop()