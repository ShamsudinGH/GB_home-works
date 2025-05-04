import math


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius**2)

    def perimeter(self):
        return  2 * math.pi * self.radius


radius = int(input('Введите радиус: '))
C1 = Circle(radius)
print(f'Площадь {C1.area()}\nПериметр {C1.perimeter()}')


class Person:
    def __init__(self, name, surname, patronimic, age):
        self.name = name
        self.surname = surname
        self.patronimic = patronimic
        self._age = int(age)

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age

    def __str__(self):
        return  f'{self.surname} {self.name} {self.patronimic} '


class Employee(Person):
    MAX_LVL = 7
    def __init__(self, name, surname, patronimic, age, id):
        super().__init__(name, surname, patronimic, age)
        self.id = id

    def get_lvl(self):
        return sum([int(num) for num in str(self.id)]) % self.MAX_LVL


class Animal:

    def __init__(self, weight, height, pet):
        self.weight = weight
        self.height = height
        self.pet = pet

    def move(self):
        print("I'm moving")


class Fish(Animal):
    def __init__(self, weight: int, height: int, pet: bool, species: str):
        super().__init__(weight, height, pet)
        self.__species = species

    def move(self):
        print("I'm swiming")

    def get_species(self):
        return self.__species


class Factory:
    def create_instance(class_name, *args):
        if class_name not in globals():
            raise ValueError(f"Класс {class_name} не найден")
        target_class = globals()[class_name]
        instance = target_class(*args)
        return instance


f1 = Factory.create_instance('Fish', 10, 20, True, 'Тунец')
f1.move()
print(f1.get_species())