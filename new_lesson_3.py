import re
from collections import Counter
import wikipedia
import itertools

def task_1(lst: list):
    return list(set([x for x in lst if lst.count(x) > 1]))


# lst = [1, 2, 3, 1, 2, 5, 6]
# print(task_1(lst))

def task_2(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words).most_common(10)


# print(task_2(wikipedia.summary("Python Programming Language")))

def task_3(items: dict, max_weight: int = 0):
    backpack_equipment = []
    for item, weight in items.items():
        if weight <= max_weight:
            backpack_equipment.append(item)
            max_weight -= weight

    return backpack_equipment

items = {'tent': 5, 'water': 3, 'food': 4, 'clothes': 2, 'first aid kit': 1}
max_weight = 10
# print(task_3(items, max_weight))
