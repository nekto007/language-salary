import os

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
