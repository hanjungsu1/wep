# import feedparser
# import webbrowser
import tkinter as tk
from urllib.request import urlopen
from bs4 import BeautifulSoup
from PIL import Image, ImageTk
from io import BytesIO

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

# 뉴스 헤드라인 출력 및 링크 출력
for link in response.find_all('a'):
    headline_text = link.text.strip()
    headline_link = link.get('href')
    headline = f"{headline_text}: {headline_link}"
    headline_label = tk.Label(root, text=headline, fg="blue", cursor="hand2")
    headline_label.pack()

# 이미지 출력을 위한 라벨 생성
image_label = tk.Label(root, text="이미지")
image_label.pack()

# 이미지 출력
for img in response.find_all('img'):
    image_src = 'http:' + img.get('src')
    # 이미지의 부모 요소인 링크의 href 가져오기
    image_link = img.find_parent('a').get('href')
    # 이미지를 다운로드하여 표시
    image_data = urlopen(image_src).read()
    image = Image.open(BytesIO(image_data))
    photo = ImageTk.PhotoImage(image)
    image_label = tk.Label(root, image=photo)  # 이미지를 출력하기 위해 text 대신 image 속성 사용
    image_label.image = photo  # 윈도우가 종료되어도 이미지가 유지되도록 함
    image_label.pack()

    # 이미지에 대한 하이퍼링크 출력
    image_link_label = tk.Label(root, text=image_link, fg="blue", cursor="hand2")
    image_link_label.pack()

# 윈도우 실행
root.mainloop()