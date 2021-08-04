import requests
from bs4 import BeautifulSoup

import argparse
from time import sleep
from collections import defaultdict
import csv

parser = argparse.ArgumentParser()
parser.add_argument(
    '--position',
    type=str,
    default=None,
    help='Position of interest. Default = None.'
)
parser.add_argument(
    '--page',
    type=int,
    default=1,
    help='Number of pages to parse. Default = 1.'
)
args = parser.parse_args()

headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
    'Accept':'*/*'
}

root_url = 'https://www.hh.ru/search/vacancy'
resume_site = 'www.hh.ru'

resume_data = defaultdict(list)

if __name__ == '__main__':
    position = args.position
    pages = args.page
    print(f'Position: {position}, page: {pages}.')

    params = {
        'area':f'',
        'APfromSearchLinePID': 'true',
        'st': 'searchVacancy',
        'text':position
    }

    for page in range(0, pages):
        params['page'] = page
        response = requests.get(root_url, headers=headers, params=params)
        print(f'Принят URL: {response.url}\nДелаем запрос по заданному url...')
        print(f'запрос выполнен, статус ответа: {response.status_code}!')
        if 200 <= response.status_code <=299:
            soup = BeautifulSoup(response.text, 'html.parser')
            print('Начинаем парсить...')
            vacancies = soup.findAll('div', {'class': 'vacancy-serp-item'})
            for vacancy in vacancies:
                resume_url = vacancy.findAll('a', {'data-qa': 'vacancy-serp__vacancy-title'})[0]['href']
                position = vacancy.findAll('a', {'data-qa': 'vacancy-serp__vacancy-title'})[0].text
                salary = vacancy.findAll('div', {'class': 'vacancy-serp-item__sidebar'})[0].text
                company_name = vacancy.findAll('a', {'data-qa': 'vacancy-serp__vacancy-employer'})[0].text
                place_company = vacancy.findAll('span', {'data-qa': 'vacancy-serp__vacancy-address'})[0].text
                min_salary, max_salary, currency = pars_salary(salary)
                resume_data['resume_site'].append(resume_site)
                resume_data['position'].append(position)
                resume_data['min_salary'].append(min_salary)
                resume_data['max_salary'].append(max_salary)
                resume_data['currency'].append(currency)
                resume_data['resume_url'].append(resume_url)
                resume_data['company_name'].append(company_name)
                resume_data['place_company'].append(place_company)
            sleep(0.2)

            #вывод датафрейма
            frame = DataFrame(resume_data)
            print(tabulate(frame, headers='keys', tablefmt='psql'))



