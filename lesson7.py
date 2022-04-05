# Задание №1

from random import randint


class Matrix:
    def __init__(self, list):
        self.li = list

    def randoms(self):
        for i in range(len(self.li)):
            for n in range(len(self.li[i])):
                self.li[i][n] = randint(0, 99)

    def __str__(self):
        result = str()
        for i in range(0, len(self.li)):
            res = '\n'
            for n in self.li[i]:
                res = res + f'  {n}'
            result = result + res
        return f'Matrix:{result}'

    def __add__(self, other):
        return Matrix([[self.li[i][n] + other.li[i][n] for n in range(len(self.li[i]))] for i in range(len(self.li))])


matrix1 = Matrix([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(matrix1)
matrix2 = Matrix([
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
])
print(matrix2)
matrix3 = matrix1 + matrix2
print(matrix3)
matrix2.randoms()
print(matrix2)
matrix3 = matrix1 + matrix2
print(matrix3)


# Задание №2

from abc import ABC, abstractmethod


class Clothe(ABC):
    def __init__(self, name):
        self.name = name

    result = 0

    @abstractmethod
    def fabric_c(self):
        return None

    def __add__(self, other):
        return f'Суммарный расход: {self.result + other.result}'


class Coat(Clothe):
    def __init__(self, name, size):
        super().__init__(name)
        self.s = size

    @property
    def fabric_c(self):
        self.result = self.s / 6.5 + 0.5
        return f'Расход материала на {self.name} составит: {self.result} едениц.'


class Jacket(Clothe):
    def __init__(self, name, height):
        super().__init__(name)
        self.h = height

    @property
    def fabric_c(self):
        self.result = 2 * self.h + 0.3
        return f'Расход материала на {self.name} составит: {self.result} едениц.'


co1 = Coat('Пальто 1', 52)
ja1 = Jacket('Костюм 1', 182)
print(co1.fabric_c)
print(ja1.fabric_c)
print(ja1 + co1)


# Задание №3


class Cell:
    def __init__(self, number):
        self.n = int(number)

    def __str__(self):
        return f'Размер клетки:\n   {self.n * "*"}'

    def __add__(self, other):
        return Cell(self.n + other.n)

    def __sub__(self, other):
        return Cell(self.n - other.n) if 0 < self.n - other.n else f'Вычитание невозможно'

    def __mul__(self, other):
        return Cell(self.n * other.n)

    def __truediv__(self, other):
        return Cell((self.n + other.n) // 2)

    def make_order(self, row):
        res = ('*' * row + '\n') * (self.n // row) + '*' * (self.n % row) if self.n >= row else '*' * self.n
        return print(f'Форма клетки:\n{res}')

c1 = Cell(8)
c2 = Cell(3)
c3 = c1 + c2
print(c3)
c4 = c1 - c2
print(c4)
c5 = c2 * c4
print(c5)
c6 = c3 - c5
print(c6)
c7 = c5 / c1
print(c7)
c7.make_order(5)
c2.make_order(5)
