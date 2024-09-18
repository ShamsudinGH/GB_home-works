import csv
import functools
import json
from random import randint
from typing import Callable
import math


def csv_decorate(func: Callable):
    @functools.wraps(func)
    def wrapper(file_name):
        results = []
        with open(file_name, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                a, b, c = map(int, row)
                results.append(func(a, b, c))
        return results
    return wrapper


def args_in_json(func: Callable):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open(f'{func.__name__}.json', 'w', encoding='utf-8') as file_json:
            json.dump({'func': func.__name__, 'args': args, 'kwargs': kwargs, 'result': result}, file_json)
        return result
    return wrapper

def find_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant >= 0 and a != 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return x1, x2
    else:
        return ("Irrational roots",)


def generate_csv(file_name):
    with open(file_name, 'w', newline='', encoding='utf-8') as f:
        nums = [[randint(0, 100) for _ in range(3)] for _ in range(randint(100, 1000))]
        csv.writer(f, dialect='excel').writerows(nums)

