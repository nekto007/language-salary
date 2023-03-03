import os

from dotenv import load_dotenv

from analytics import predict_salary

load_dotenv()
HH_API_BASE_URL = os.getenv("HH_API_BASE_URL")


def predict_rub_salary_hh(vacancy: dict):
    salary = vacancy.get('salary')
    salary_from = salary.get('from')
    salary_to = salary.get('to')
    if salary.get("currency") == "RUR":
        predict_salary(salary_from, salary_to)
