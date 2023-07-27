import math
from decimal import Decimal


def task_1():
    b = int(input('Введите b: '))
    c = int(input('Введите c: '))
    a = int(input('Введите a: '))

    if (a + b > c) and (a + c > b) and (b + c > a):
        if a == b == c:
            print('Треугольник равносторонний')
        elif a == b or a == c or b == c:
            print('Треугольник равнобедренный')
        else:
            print('Треугольник разносторонний')
    else:
        print('Такого треугольника не существует')

# task_1()

def task_2(a):
    check = all(a % i for i in range(2, round(math.sqrt(a)+1)))
    if check:
        print('Число простое!')
    else:
        print('Число не является простым.')

# task_2(int(input('Введите число для проверки ')))

def task_3():
    number_1 = Decimal(input('Введите число: '))
    after_float = round((number_1 % 1) * 10**(number_1.as_tuple().exponent*(-1)))
    befor_float = number_1 // 1
    sum_numbers = 0

    while after_float > 0:
        sum_numbers += after_float % 10
        after_float //= 10

    while befor_float > 0:
        sum_numbers += befor_float % 10
        befor_float //= 10

    print(sum_numbers)

# task_3()