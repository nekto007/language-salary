from terminaltables import AsciiTable

from analytics import get_statistics
from headhunter import fetch_vacancies_from_hh, predict_rub_salary_hh
from superjob import fetch_vacancies_from_sj, predict_rub_salary_sj


def main():
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
        vacancies_from_hh = fetch_vacancies_from_hh(language)
        predict_salaries_from_hh = [predict_rub_salary_hh(vacancy) for vacancy in vacancies_from_hh]
        stats_from_hh.append(get_statistics(language, vacancies_from_hh, predict_salaries_from_hh))

        vacancies_from_sj = fetch_vacancies_from_sj(language)
        predict_salaries_from_sj = [predict_rub_salary_sj(vacancy) for vacancy in vacancies_from_sj]
        stats_from_sj.append(get_statistics(language, vacancies_from_sj, predict_salaries_from_sj))

    table_instance_hh = AsciiTable(stats_from_hh, title='HeadHunter Moscow')
    print(table_instance_hh.table)
    print()
    table_instance_sj = AsciiTable(stats_from_sj, title='SuperJob Moscow')
    print(table_instance_sj.table)
    print()


if __name__ == '__main__':
    main()
