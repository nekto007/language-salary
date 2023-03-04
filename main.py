from dotenv import load_dotenv
from terminaltables import AsciiTable
import os
from analytics import get_statistics
from headhunter import fetch_vacancies_from_hh, predict_rub_salary_hh
from superjob import fetch_vacancies_from_sj, predict_rub_salary_sj


def main():
    load_dotenv()
    hh_api_base_url = "https://api.hh.ru/vacancies/"
    sj_api_base_url = "https://api.superjob.ru/2.0/vacancies/"
    superjob_token = os.getenv("SUPERJOB_TOKEN")
    table_headers = [
        "Язык программирования",
        "Вакансий найдено",
        "Вакансий обработано",
        "Средняя зарплата",
    ]

    languages = [
        "TypeScript",
        "Scala",
        "JavaScript",
        "Python",
        "Ruby",
        "Go",
        "Objective-C",
        "Java",
        "Kotlin",
        "C#",
        "Swift",

    ]
    stats_from_hh, stats_from_sj = [table_headers], [table_headers]
    for language in languages:
        vacancies_from_hh = fetch_vacancies_from_hh(language, hh_api_base_url)
        salaries_from_hh = [predict_rub_salary_hh(vacancy) for vacancy in vacancies_from_hh]
        stats_from_hh.append(get_statistics(language, vacancies_from_hh, salaries_from_hh))

        vacancies_from_sj = fetch_vacancies_from_sj(language, superjob_token, sj_api_base_url)
        salaries_from_sj = [predict_rub_salary_sj(vacancy) for vacancy in vacancies_from_sj]
        stats_from_sj.append(get_statistics(language, vacancies_from_sj, salaries_from_sj))

    table_instance_hh = AsciiTable(stats_from_hh, title='HeadHunter Moscow')
    print(table_instance_hh.table)
    print()
    table_instance_sj = AsciiTable(stats_from_sj, title='SuperJob Moscow')
    print(table_instance_sj.table)
    print()


if __name__ == '__main__':
    main()
