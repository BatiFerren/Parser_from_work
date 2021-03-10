import requests
from bs4 import BeautifulSoup as bSoup
import csv


def write_csv(data):
    with open('companies.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['name'], data['url']))


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
        data = {'name': name, 'url': company_url}
        print(data)
        write_csv(data)


def main():
    url = 'https://www.work.ua/ru/jobs/by-company/'
    html = get_html(url)
    get_page_data(html)


if __name__ == '__main__':
    main()
