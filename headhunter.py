from itertools import count

import requests

from analytics import predict_salary

MOSCOW_AREA = 1
PERIOD_IN_DAYS = 30


def predict_rub_salary_hh(vacancy: dict):
    salary = vacancy.get('salary')
    if salary is None:
        return None
    elif salary.get("currency") == "RUR":
        salary_from = salary.get('from')
        salary_to = salary.get('to')
        return predict_salary(salary_from, salary_to)


def fetch_vacancies_from_hh(language, base_url):
    url = base_url
    vacancies = []
    for page in count(0):
        params = {
            "area": MOSCOW_AREA,
            "period": PERIOD_IN_DAYS,
            "text": f'программист {language}',
            "page": page
        }
        response = requests.get(url, params)
        response.raise_for_status()
        vacancies_page = response.json()
        vacancies.extend(vacancies_page['items'])

        if page >= vacancies_page['pages'] or page == 99:  # "You can't look up more than 2000 items in the list"
            break
    return vacancies
