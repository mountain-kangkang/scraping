# 순위 1~100 노래 정보 가져오기
# 순위, 노래 제목, 가수, 앨범정보
# chat-GPT 사용해서 결과를 html에 화면에 재구성해보기(플라스크와 진자탬플릿 사용 or 부트스트랩도 괜찮을듯)

import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"}

url = "https://www.melon.com/chart/index.htm"
req = requests.get(url, headers=header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")

# result = soup.select(".lst50, .lst100")
# result = soup.find_all(class_= ["lst50", "lst100"])
results = soup.select(".lst50") + soup.select(".lst100")        # 1~50위, 51~100위 까지
song_rank = []
for result in results:
    rank = result.select_one(".rank").text.replace("\n", "")
    title = result.select_one(".rank01").text.replace("\n", "")
    singer = result.select_one(".checkEllipsis").text.replace("\n", "")
    album = result.select_one(".rank03").text.replace("\n", "")
    img = result.select_one("img")["src"]
    song_rank.append({
        "rank":rank,
        "title":title,
        "singer":singer,
        "album":album,
        "photo":img
    })
