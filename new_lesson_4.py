from random import randint



def task_1(k):
    s = [[0 for _ in range(len(k))] for _ in range(len(k[0]))]
    for i in range(len(k)):
        for j in range(len(k[0])):
            s[j][i] = k[i][j]
    return s


list_1 = [[randint(0, 9) for _ in range(3)] for _ in range(3)]
for i in list_1:
    print(i)
print('')
for i in task_1(list_1):
    print(i)


def task_2(**kwargs):
    ret = {}
    for k, v in kwargs.items():
        ret[f'{hash(v)}'] = k
    return ret


# print(task_2())



