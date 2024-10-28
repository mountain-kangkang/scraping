import requests
from bs4 import BeautifulSoup

keyword = input("검색할 상품 : ")
url = f"https://www.coupang.com/np/search?component=&q={keyword}"

header_user = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36","accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
req = requests.get(url, timeout=5, headers=header_user)

html = req.text
soup = BeautifulSoup(html, 'html.parser')

items = soup.select('.search-product')

# 1위부터 10위까지의 상품 정보
for index, item in enumerate(items, 1):
    if item.select_one(f'.number'):
        rank = item.select_one(f'.number').text.strip()
        name = item.select_one('.name').text
        price = item.select_one('.price-value').text
        link = item.select_one('a')['href']
        img_src = item.select_one('.search-product-wrap-img')['src'].replace("230x230","600x600")
        rocket = item.select_one('.badge.rocket')

        print(f'[{rank} 위]')
        print(f'상품명 : {name}')
        print(f'가격 : {price}')
        print(f'링크 : https://www.coupang.com{link}')
        print(f'이미지링크 : https:{img_src}')
        if rocket:
            print("로켓베송 가능!!!")
        print()
        

        img_req = requests.get('https:'+img_src)
        with open(f"/Users/mac/Desktop/for_scraping/task_3/img/{rank}.jpg","wb") as f:
            f.write(img_req.content)