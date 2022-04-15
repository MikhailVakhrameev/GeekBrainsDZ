# Задание №1


class Date:
    def __init__(self,date):
        self.d = date

    @classmethod
    def dat(cls,li):
        date = [int(i) for i in li.split('-')]
        return cls(date)


    @staticmethod
    def val(dat):
        date = [int(i) for i in dat.split('-')]
        if 0 < date[0] < 31 and 0 < date[1] < 12 and 1900 < date[2] < 2023:
            print(f'Дaта {dat} верна')
        else:
            print(f'Введите дату в формате "ДД-ММ-ГГГГ"')


da1 = '11-11-11'
da2 = '11-11-2001'
d1 = Date.dat(da1)
print(d1.d)
d2 = Date.val(da1)
d3 = Date.val(da2)


# Задание №2


class Division(Exception):
    def __init__(self, txt):
        self.t = txt


a = input('Введите число: ')
try:
    if int(a) == 0:
        raise Division('Деление на 0 невозможно')
    res = 15 / int(a)
except ValueError:
    print(f'{a} не является числом')
except Division as err:
    print(err)
else:
    print(res)


# Задание №3


class ExceptionVal(Exception):
    def __init__(self, txt):
        self.t = txt

my_li = []
while True:
    number = input('Введите число или "s" для завершения: ')
    if number == 's' or number == 'S':
        break
    else:
        try:
            for i in number:
                if i not in '1234567890':
                    raise ExceptionVal('Вводить можно только числа')
        except ExceptionVal as err:
            print(err)
        else:
            my_li.append(int(number))
    print(my_li)
print(my_li)


# Задание №4,5,6


class Warehouse():
    def __init__(self, name):
        self.name = name
        self.items = []

    def __str__(self):
        res = f'В наличии на складе: "{self.name}":\n'
        if self.items:
            for i, item in enumerate(self.items):
                res += f"{i}: {item}\n"
        else:
            res += 'На складе ничего нет\n'
        return res

    def add(self, equipment):
        self.items.append(equipment)

    def turn_down(self, equipment):
        self.items.remove(equipment)

    def move(self, equip, other):
        self.turn_down(equip)
        other.add(equip)


class Product():
    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount

    def __str__(self):
        return f'{self.name} цена: {self.price} колличество: {self.amount}шт.'


class Printer(Product):
    pass

class Scanner(Product):
    pass

class Xerox(Product):
    pass



e1 = Printer('Printer', 10000, 2)
e2 = Scanner('Scanner', 20000, 4)
e3 = Xerox('Xerox', 30000, 1)

w1 = Warehouse('w1')
w2 = Warehouse('w2')

w1.add(e1)
w1.add(e2)
w1.add(e3)

print(w1)
w1.move(e1, w2)
w1.move(e2, w2)
print(w1)
w1.move(e3, w2)
print(w2)

# Задание №7


class Complex:
    def __init__(self, real, image):
        self.r = real
        self.i = image

    def __add__(self, other):
        return Complex(self.r + other.r, self.i + other.i)

    def __mul__(self, other):
        return Complex(self.r * other.r - self.i * other.i, self.i * other.r + self.r * other.i)

    def __str__(self):
        return f'Complex = {self.r},{self.i}'


c1 = Complex(1, -1)
c2 = Complex(0, 1)
c3 = Complex(-1, 1)

print(c1 + c2)
print(c1 * c2)
print(c2 * c3)
