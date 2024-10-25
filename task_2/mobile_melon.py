from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

user = "Mozilla/5.0 (IPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15(KHTML, like Gecko) CriOS/80.0.3987.95 Mobile/15E148 Safari/604.1"

options_ = Options()
options_.add_argument(f"user-agent={user}")
options_.add_experimental_option("detach", True)
options_.add_experimental_option("excludeSwitches", ["enable-logging"])


#크롬 드라이버 매니저를 자동으로 설치되도록 실행시키는 코드
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options_)

url = "https://m2.melon.com/index.htm"
driver.get(url)
time.sleep(0.7)

driver.find_element(By.CSS_SELECTOR, '.link-logo').click()
time.sleep(0.6)

driver.find_element(By.XPATH, '//a[text()="멜론차트"]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//button[@onclick="hasMore2();"]').click()
time.sleep(0.3)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
results = soup.select(".list_item")
for result in results:
    if result.select_one('.ranking_num'):
        rank = result.select_one('.ranking_num').text
        title = result.select_one('p[class*=title]').text.lstrip().rstrip()
        singer = result.select_one('.name.ellipsis').text

        print("순위 : ", rank)
        print("노래 : ", title)
        print("가수 : ", singer)
        print()


driver.quit()