import feedparser
import tkinter as tk

def scrape_and_display():
    # 네이버 뉴스 RSS 피드 URL
    rss_url = 'https://news.naver.com/main/home.naver/rss.nhn'

    # 웹 페이지 가져오기
    response = feedparser.parse(rss_url)

    # HTML 파싱
    soup = BeautifulSoup(response.text, 'html.parser')

    # 각 뉴스 헤드라인을 리스트에 추가
    for entry in feed.entries:
        headlines.append(entry.title)

    # 리스트에 있는 뉴스 헤드라인을 라벨에 출력
    for idx, headline in enumerate(headlines):
        label = tk.Label(root, text=f"{idx + 1}. {headline}")
        label.pack()

# Tkinter 윈도우 생성
root = tk.Tk()
root.title(" 뉴스 헤드라인")

# 스크래핑 및 화면 출력 버튼 생성
scrape_button = tk.Button(root, text="네이버 뉴스 헤드라인 가져오기", command=scrape_and_display)
scrape_button.pack()

# 윈도우 실행
root.mainloop()