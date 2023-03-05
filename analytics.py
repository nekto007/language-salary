def predict_salary(salary_from: int, salary_to: int):
    if salary_from and salary_to:
        return int((salary_from + salary_to) / 2)
    elif not salary_to:
        return int(salary_from * 1.2)
    elif not salary_from:
        return int(salary_to * 0.8)


def get_statistics(language, vacancies, predict_salaries):
    salary_filtered = [salary for salary in predict_salaries if salary]
    vacancies_found = len(vacancies)
    vacancies_processed = len(salary_filtered)

    if salary_filtered:
        average_salary = str(sum(salary_filtered) // len(salary_filtered))
    else:
        average_salary = '-'

    return [language, vacancies_found, vacancies_processed, average_salary]
