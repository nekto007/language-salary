import os

import requests
from dotenv import load_dotenv

from analytics import predict_salary

load_dotenv()
SJ_API_BASE_URL = os.getenv("SJ_API_BASE_URL")
SUPERJOB_TOKEN = os.getenv("SUPERJOB_TOKEN")


def predict_rub_salary_sj(vacancy: dict):
    salary_from = vacancy.get('payment_from')
    salary_to = vacancy.get('payment_to')
    if vacancy.get("currency") == "rub":
        return predict_salary(salary_from, salary_to)


def fetch_vacancies_from_sj(language):
    headers = {'X-Api-App-Id': SUPERJOB_TOKEN}
    url = SJ_API_BASE_URL
    params = {
        'catalogues': 33,
        'no_agreement': 1,
        'town': 4,
        'keyword': language,
    }
    page = 0
    more_pages = True
    vacancies = []
    while more_pages:
        params['page'] = page
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data_vacancies = response.json()
        more_pages = data_vacancies['more']
        vacancies.extend(data_vacancies['objects'])
        page += 1
    return vacancies
