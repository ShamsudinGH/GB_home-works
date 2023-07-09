# Задача 34:

def task_34(words):
    str = words.lower().split()
    s = lambda x: len([1 for i in x if i in 'аоуыэеёиюя'])
    l = list(map(s, str))
    if max(l) == min(l):
        print('Парам пам-пам')
    else:
        print('Пам парам')

task_34(input('Введите фразу для проверки на ритм: '))


# Задача 36

def print_operation_table(operation, num_rows=6, num_columns=6):
    f = [[operation(i,j) for i in range(1, num_rows+1)] for j in range(1, num_columns +1)]
    for i in f:
        print(*i)

# print_operation_table(lambda x, y: x * y)
