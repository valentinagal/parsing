from bs4 import BeautifulSoup as bs
import requests
from pprint import pprint

url = 'https://hh.ru'

params = {'quick_filters':'vacancy',
          'query':'актер',
          'tab':'all'}

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}

response = requests.get(url+'/vacancies/akter', params=params, headers=headers)

soup = bs(response.text, 'html.parser')

vacancies_list = soup.find_all('div', attrs={'class':'vacancy-serp-item__info'})
print()

vacancies = []

for vacancy in vacancies_list:
    vacancy_data = {}
    vacancy_name = vacancy.find('a', attrs={'data-qa': 'vacancy-serp__vacancy-title'}).getText()

    vacancy_link = url + vacancy.find('a', attrs={'data-qa':'vacancy-serp__vacancy-title'}).get('href')

    vacancy_salary = vacancy.find('div', attrs={'class':'vacancy-serp-item__sidebar'}).children.getText()



    vacancy_data['link'] = vacancy_link
    vacancy_data['name'] = vacancy_name
    vacancy_data['salary'] = vacancy_salary

    vacancies.append(vacancy_data)

pprint(vacancies)