def predict_salary(salary_from: int, salary_to: int):
    if salary_from and salary_to:
        return int((salary_from + salary_to) / 2)
    elif salary_to is None:
        return int(salary_from * 1.2)
    elif salary_from is None:
        return int(salary_to * 0.8)


def get_statistics(language, vacancies, predict_salaries):
    predict_salaries = [predict_salary for predict_salary in predict_salaries if predict_salary]
    vacancies_found = len(vacancies)
    vacancies_processed = len(predict_salaries)

    if predict_salaries:
        average_salary = str(sum(predict_salaries) // len(predict_salaries))
    else:
        average_salary = '-'

    return [language, vacancies_found, vacancies_processed, average_salary]
