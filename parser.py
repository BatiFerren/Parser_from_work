import requests
from bs4 import BeautifulSoup as bSoup
import csv


def get_html(url):
    r = requests.get(url)
    if r.ok:
        return r.text
    print(r.status_code)


def get_page_data(html):
    soup = bSoup(html, 'lxml')
    companies = soup.find('ul', class_ = 'logotypes-squares').find_all('li')
    for company in companies:
        name = company.find('a').find('h5').text
        company_url = 'https://www.work.ua' + company.find('a').get('href')
        print(company_url)


def main():
    url = 'https://www.work.ua/ru/jobs/by-company/'
    get_page_data(get_html(url))


if __name__ == '__main__':
    main()