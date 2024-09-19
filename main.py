import requests
from bs4 import BeautifulSoup

url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs#job-listings"


response = requests.get(url)
# print(response.content)

# Beautiful soup로 html parsing
soup = BeautifulSoup(response.content, "html.parser")

jobs = soup.find("section", class_="jobs").find_all("li")[1:-1]

for job in jobs:
    title = job.find("span", class_="title")
    company, position, region = job.find_all("span", class_="company")
    company = company.text
    position = position.text
    region = region.text
    print(f"{company}  {position}  {region}")
