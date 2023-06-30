def task_26 (a, b):
    if b == 0:
        return 1
    return a * task_26(a, b-1)

# print(task_26(3, 5))

def task_28(a, b):
    if b == 0:
        return a
    else:
        return task_28(a + 1, b - 1)
    
# print(task_28(2, 2))
