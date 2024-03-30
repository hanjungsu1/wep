import feedparser
import tkinter as tk
import webbrowser

def scrape_and_display():
    # Daum 뉴스 RSS 피드 URL
    url = "http://media.daum.net/syndication/today_sisa.rss"

    # 웹 페이지 가져오기
    response = feedparser.parse(url)

    # 리스트에 있는 뉴스 헤드라인을 라벨에 출력
    for idx, headline in enumerate(response.entries):
        headline = entry.title
        link = entry.link
        print(f"{idx + 1}. {entry.title}")
        print(f"    Link: {link}")
        print()

        # 기사 링크를 웹 브라우저에서 열기
        webbrowser.open(link)
    
# 스크래핑 함수 호출
scrape_and_display()