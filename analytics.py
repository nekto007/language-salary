def predict_salary(salary_from: int, salary_to: int):
    if salary_from and salary_to:
        return int((salary_from + salary_to) / 2)
    elif not salary_to:
        return int(salary_from * 1.2)
    elif not salary_from:
        return int(salary_to * 0.8)


def get_statistics(language, vacancies, salaries):
    filtered_salary = [salary for salary in salaries if salary]
    vacancies_found = len(vacancies)
    vacancies_processed = len(filtered_salary)

    if filtered_salary:
        average_salary = str(sum(filtered_salary) // len(filtered_salary))
    else:
        average_salary = '-'

    return [language, vacancies_found, vacancies_processed, average_salary]
