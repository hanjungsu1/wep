import feedparser
import tkinter as tk
import webbrowser

def open_news_link(likn):
    webbrowser.open(link)

def scrape_and_display():
    # Daum 뉴스 RSS 피드 URL
    url = "http://media.daum.net/syndication/today_sisa.rss"

    # 웹 페이지 가져오기
    response = feedparser.parse(url)

    # 뉴스 헤드라인 리스트 초기화
    headlines = []

    # 각 뉴스 헤드라인을 리스트에 추가
    for entry in response.entries:
        headlines = entry.title
        link = entry.link
        headlines.append((headline, link))

    # 리스트에 있는 뉴스 헤드라인을 라벨에 출력
    for idx, headline in enumerate(headlines):
        label = tk.Label(root, text=f"{idx + 1}. {headline}", fg="blue", cursor="hand2")
        label.bind("<Button-1>", lambda e, link=link: open_news_link(link))
        label.pack()
    


# Tkinter 윈도우 생성
root = tk.Tk()
root.title(" 뉴스 헤드라인")

# 스크래핑 및 화면 출력 버튼 생성
scrape_button = tk.Button(root, text="Daum 뉴스 헤드라인 가져오기", command=scrape_and_display)
scrape_button.pack()

# 윈도우 실행
root.mainloop()