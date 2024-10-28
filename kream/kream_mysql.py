from selenium import webdriver
from bs4 import BeautifulSoup
import pymysql

# selenium에 다양한 옵션을 적용시키기 위한 패키지
from selenium.webdriver.chrome.options import Options
# CLASS, ID를 CSS_SELECTOR를 이용하기 위한 패키지
from selenium.webdriver.common.by import By
# 키보드의 입력 형태를 코드로 작성하기 위한 패키지
from selenium.webdriver.common.keys import Keys

import time

user = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"}
options_ = Options()
options_.add_argument(f'User_Agent={user}')
options_.add_experimental_option('detach', True)
# Chrome이 자동화된 테스트 소프트웨어에 의해 제어되고 있습니다. 팝업창을 제거하기 위한 코드(아래) 난 별로 사용하고싶지안다. 적용도 잘 안되고...
# options_.add_experimental_option('excludeSwitches', ['enable-logger'])

driver = webdriver.Chrome(options=options_)

url = 'https://kream.co.kr/'
driver.get(url)
time.sleep(0.5)
                                        # 클래스 명이 3개임
driver.find_element(By.CSS_SELECTOR, '.btn_search.header-search-button.search-button-margin').click()
time.sleep(0.5)

driver.find_element(By.CSS_SELECTOR, '.input_search.show_placeholder_on_focus').send_keys('Supreme')
time.sleep(0.4)
driver.find_element(By.CSS_SELECTOR, '.input_search.show_placeholder_on_focus').send_keys(Keys.ENTER)
time.sleep(0.4)

for i in range(20):
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    time.sleep(0.4)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
items = soup.select('.product_card')

product_list = []
for item in items:
    product_name = item.select_one('.translated_name').text
    # print(product_name)
    if '후드' in product_name:
        category = '상의'
        product_brand = item.select_one('.product_info_brand.brand').text
        product_price = item.select_one('.amount').text

        # print(f'product : {product_name}')
        # print(f'category : {category}')
        # print(f'brand : {product_brand}')
        # print(f'price : {product_price}')
        # print()
        temp = [category, product_brand, product_name, product_price]
        product_list.append(temp)

driver.quit()

# 과제 brand 입력 -> 카테고리 클릭(프로그램에서 input()으로 카테고리 검색하는 기능도 있다) -> 스크랩핑

connection = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='0000',
    db='kream',
    charset='utf8mb4'
)

connection.cursor()
def excute_query(connection, query, args=None):
    with connection.cursor() as cursor:
        cursor.execute(query, args or ())
        if query.strip().upper().startswith('SELECT'):
            return cursor.fetchall()
        else:
            connection.commit()

for i in product_list:
    excute_query(connection, "INSERT INTO kream(category, brand, product_name, price) VALUES (%s, %s, %s, %s)", (i[0], i[1], i[2], i[3]))