from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup

p = sync_playwright().start()
browser = p.chromium.launch(headless=False)

page = browser.new_page()

url = "https://www.wanted.co.kr"

page.goto(url)

time.sleep(3)

page.click("button.Aside_searchButton__rajGo")

time.sleep(3)

page.get_by_placeholder("검색어를 입력해 주세요.").fill("flutter")

time.sleep(3)

page.keyboard.down("Enter")

time.sleep(3)

page.click("a#search_tab_position")

for x in range(3):

    time.sleep(3)

    page.keyboard.down("End")

time.sleep(3)

full_html = page.content()

p.stop()

soup = BeautifulSoup(full_html, "html.parser")

jobs = soup.find_all(
    "div", class_="JobCard_container__REty8 JobCard_container--variant-card__gaJS_"
)

job_list = []
for job in jobs:
    link = f"{url}{job.find('a')['href']}"
    title = job.find("strong", class_="JobCard_title__HBpZf").text
    company = job.find("span", class_="JobCard_companyName__N1YrF").text
    job_temp = {"link": link, "title": title, "company": company}
    job_list.append(job_temp)
    print(job_temp)
