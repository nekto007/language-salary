import requests

from analytics import predict_salary

SALARY_NO_AGREEMENT = 1
MOSCOW_ID = 4
IT_SECTION = 33


def predict_rub_salary_sj(vacancy: dict):
    salary_from = vacancy.get('payment_from')
    salary_to = vacancy.get('payment_to')
    if vacancy.get("currency") == "rub":
        return predict_salary(salary_from, salary_to)


def fetch_vacancies_from_sj(language, superjob_token, sj_api_base_url):
    headers = {'X-Api-App-Id': superjob_token}
    url = sj_api_base_url
    params = {
        'catalogues': IT_SECTION,
        'no_agreement': SALARY_NO_AGREEMENT,
        'town': MOSCOW_ID,
        'keyword': language,
    }
    page = 0
    more_pages = True
    vacancies = []
    while more_pages:
        params['page'] = page
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        vacancies_page = response.json()
        more_pages = vacancies_page['more']
        vacancies.extend(vacancies_page['objects'])
        page += 1
    return vacancies
