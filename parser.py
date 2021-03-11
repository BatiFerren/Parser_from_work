import requests
from bs4 import BeautifulSoup as bSoup
import csv


#TODO: Need to change writer for write Dictionary. Use csv.DictWriter()
'''def write_csv(data):
    with open('companies.csv', 'a') as f:
        columns = ['name', 'url']
        writer = csv.DictWriter(f, fieldnames=columns)
        #writer.writeheader()
        writer.writerow(data)
'''


def get_html(url):
    r = requests.get(url)
    if r.ok:
        return r.text
    print(r.status_code)


def get_page_data(html):
    company_list = []
    soup = bSoup(html, 'lxml')
    companies = soup.find('ul', class_ = 'logotypes-squares').find_all('li')
    for company in companies:
        name = company.find('a').find('h5').text
        company_url = 'https://www.work.ua' + company.find('a').get('href')
        data = {'name': name, 'url': company_url}
        company_list.append(data)
    return company_list


def get_company_data(list_of_companies):
    list_of_companies_data = []
    for item in list_of_companies:
        new_request = requests.get(item['url'])
        if new_request.ok:
            company_soup = bSoup(new_request.text, 'lxml')
            name_of_company = company_soup.find('h1').text
            website_of_company = company_soup.find('span', class_ = 'website-company')
            if website_of_company:
                website = website_of_company.find('a').get('href')
            else:
                website = None
            glyphicon_phone = company_soup.find('span', class_ = 'glyphicon-phone')
            if glyphicon_phone:
                tel_contact = glyphicon_phone.find_parent('p')
            else:
                tel_contact = None
            if tel_contact:
                tel_a = tel_contact.find('a')
            else:
                tel_a = None
            if tel_a:
                tel = tel_a.text
            else:
                tel = None
            data_company = {'name': name_of_company, 'website': website, 'phone': tel}
            list_of_companies_data.append(data_company)
            #print(data_company)
    return list_of_companies_data


def main():
    url = 'https://www.work.ua/ru/jobs/by-company/'
    html = get_html(url)
    all_list = get_page_data(html)
    print_list = get_company_data(all_list)
    print(print_list)



if __name__ == '__main__':
    main()
