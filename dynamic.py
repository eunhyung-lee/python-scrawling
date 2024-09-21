from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup

p = sync_playwright().start()
browser = p.chromium.launch(headless=False)

page = browser.new_page()

url = "https://www.wanted.co.kr/"

page.goto(url)

time.sleep(3)

page.click("button.Aside_searchButton__rajGo")

time.sleep(3)

page.get_by_placeholder("검색어를 입력해 주세요.").fill("flutter")

time.sleep(3)

page.keyboard.down("Enter")

time.sleep(3)

page.click("a#search_tab_position")

for x in range(5):

    time.sleep(3)

    page.keyboard.down("End")

time.sleep(3)

full_html = page.content()

p.stop()

soup = BeautifulSoup(full_html, "html.parser")
