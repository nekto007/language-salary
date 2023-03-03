def predict_salary(salary_from: int, salary_to: int):
    if salary_from and salary_to:
        return int((salary_from + salary_to) / 2)
    elif salary_to is None:
        return int(salary_from * 1.2)
    elif salary_from is None:
        return int(salary_to * 0.8)
