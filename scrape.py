import requests
from bs4 import BeautifulSoup

URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=San-Jose'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='ResultsContainer')
# print(results.prettify())

job_seeks = results.find_all('section', class_='card-content')
for job_seek in job_seeks:
    title_seek = job_seek.find('h2', class_='title')
    company_seek = job_seek.find('div', class_='company')
    location_seek = job_seek.find('div', class_='location')
    if None in (title_seek, company_seek, location_seek):
        continue
    print(title_seek.text.strip())
    print(company_seek.text.strip())
    print(location_seek.text.strip())
    print()