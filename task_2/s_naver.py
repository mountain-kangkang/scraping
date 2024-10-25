# pip install selenium
# pip install webdriver-manager
from selenium import webdriver
from bs4 import BeautifulSoup
import time

base_url = "https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query="
keyword = input("검색어를 입력해주세요 : ")
url = base_url + keyword

browser = webdriver.Chrome()
browser.get(url)

for i in range(5):
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(1)

html = browser.page_source
soup = BeautifulSoup(html, "html.parser")

results = soup.select(".view_wrap")
for i, result in enumerate(results, 1):
    title = result.select_one(".title_link").text
    link = result.select_one(".title_link")["href"]
    writer = result.select_one(".name").text
    dsc = result.select_one(".dsc_link").text

    print(f'{i}번째 블로그')
    print(f"제목 : {title}")
    print(f"작성자 : {writer}")
    print(f"링크 : {link}")
    print(f"내용 : {dsc}")
    print()