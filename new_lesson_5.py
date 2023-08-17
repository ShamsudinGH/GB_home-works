def task_1_fib(n):
    a, b = 0, 1
    for __ in range(n):
        yield a
        a, b = b, a + b


# n = int(input('Введите N: '))
# for i in task_1_fib(n):
#     print(i)


def task_salary_dict(names_list, salaries_list, bonuses_list):
    return {name: salary * (1 + float(bonus.strip('%')) / 100) \
            for name, salary, bonus in zip(names_list, salaries_list, bonuses_list)}

names = ["Антон", "Дима", "Вазген"]
salaries = [10000, 20000, 30000]
premium = ["10%", "15%", "20%"]

# salary_dict = generate_salary_dict(names, salaries, premium)
# print(salary_dict)


import os

def parse_path(path):
    filepath, file_extension = os.path.splitext(path)
    dirname, filename = os.path.split(filepath)
    return (dirname, filename, file_extension)

# print(parse_path(os.path.abspath(input('Введите имя файла с расширением: '))))