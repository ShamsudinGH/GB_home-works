def task_16 ():
    a = []
    n = int(input('Введите n: '))
    print('Заполним массив!')
    for i in range(n):
        a.append(int(input(f'{i+1} элемент массива: ')))
    schet = 0
    x = int(input('Число Х: '))
    for i in range(n):
        if i == x:
            schet += 1
    return schet

# print(task_16())

def task_18():
    a = []
    n = int(input('Введите n: '))
    print('Заполним массив!')
    for i in range(n):
        a.append(int(input(f'{i+1} элемент массива: ')))
    x = int(input('Число Х: '))
    flag = abs(x - a[0])
    closest = 0
    for i in a:
        if abs(x - i) < flag:
            closest = i
            flag = abs(x-i)
    return closest

# print(task_18())

def task_20():
    engl = {'AEIOULNSTR' : 1,
      	'DG' : 2,
      	'BCMP' : 3,
      	'FHVWY' : 4,
      	'K' : 5,
      	'JZ' : 8,
      	'QZ' : 10}
    ru = {'АВЕИНОРСТ' : 1,
      	'ДКЛМПУ' : 2,
      	'БГЁЬЯ' : 3,
      	'ЙЫ' : 4,
      	'ЖЗХЦЧ' : 5,
      	'ШЭЮ' : 8,
      	'ФЩЪ' : 10}
    
    e_o_r = int(input('Выберите язык. Английский - "1" Русский - "2" '))
    s = input('Введите слово: ')
    if e_o_r == 1:
        return sum([v for i in s for k, v in engl.items() if i in k])
    elif e_o_r == 2:
        return sum([v for i in s for k, v in ru.items() if i in k])
    else:
        print('Некорректный запрос :(')

# print(task_20())