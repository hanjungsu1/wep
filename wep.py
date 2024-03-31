# import feedparser
# import webbrowser
import tkinter as tk
from urllib.request import urlopen
from bs4 import BeautifulSoup


# Tkinter 윈도우 생성
root = tk.Tk()
root.title("Daum 뉴스")

# Daum 뉴스 RSS 피드 URL
url = urlopen("http://media.daum.net")

# 웹 페이지 가져오기
response = BeautifulSoup(url, "html.parser")

# 뉴스 헤드라인 출력을 위한 라벨 생성
headline_label = tk.Label(root, text="뉴스 헤드라인")
headline_label.pack()

# 뉴스 헤드라인 출력
for link in response.find_all('a'):
    headline_text = link.text.strip()
    headline_link = link.get('href')
    headline = f"{headline_text}: {headline_link}"
    headline_label = tk.Label(root, text=headline)
    headline_label.pack()

# 이미지 출력을 위한 라벨 생성
image_label = tk.Label(root, text="이미지")
image_label.pack()

# 이미지 출력
for img in response.find_all('img'):
    image_src = img.get('src')
    image_label = tk.Label(root, text=image_src)
    image_label.pack()

# 윈도우 실행
root.mainloop()