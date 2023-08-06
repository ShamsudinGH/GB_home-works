import math
import decimal as dec

dec.getcontext().prec = 42
def task_1(d: dec.Decimal = 0):
    if d < 1000:
        r = dec.Decimal(d) / 2
        print(f"{r ** 2 * dec.Decimal(math.pi)}")
        print(f"{r * 2 * dec.Decimal(math.pi)}")

# print(task_1(int(input('Введите диаметр: '))))
def task_2(num):
    hex_digits = "0123456789abcdef"
    hex_str = ""
    while num > 0:
        hex_str = hex_digits[num % 16] + hex_str
        num = num // 16
    return f'16-ричное представление данного числа {hex_str}'

# print(task_2(int(input('Введите число для перевода в 16ричную систему'))))

def task_3(s_1: str= '0/1', s_2: str= '0/1'):
    l_1 = [int(i) for i in s_1.split('/')]
    l_2 = [int(i) for i in s_2.split('/')]

    sum_frac = ((l_1[0] * l_2[1] + l_1[1] * l_2[0]), (l_1[1] * l_2[1]))
    prod_frac = ((l_1[0] * l_2[0]), l_1[1] * l_2[1])
    print(sum_frac)
    print(prod_frac)

# task_3(input('Первая простая дробь '), input(f'Вторая простая дробь '))

