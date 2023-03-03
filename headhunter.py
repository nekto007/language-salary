import os
from itertools import count

from dotenv import load_dotenv

from analytics import predict_salary

load_dotenv()
HH_API_BASE_URL = os.getenv("HH_API_BASE_URL")


def predict_rub_salary_hh(vacancy: dict):
    salary = vacancy.get('salary')
    salary_from = salary.get('from')
    salary_to = salary.get('to')
    if salary.get("currency") == "RUR":
        return predict_salary(salary_from, salary_to)


def fetch_vacancies_from_hh(language):
    import requests
    url = HH_API_BASE_URL
    vacancies = []
    for page in count(0):
        params = {
            "area": 1,
            "period": 30,
            "only_with_salary": True,
            "text": f'программист {language}',
            "page": page
        }
        response = requests.get(url, params)
        response.raise_for_status()
        data_vacancies = response.json()
        vacancies.extend(data_vacancies['items'])
        if page >= data_vacancies['pages']:
            break
    return vacancies
