# Задание №1


from time import sleep


class TrafficLight:
    __color = ['Красный', 'Жёлтый', 'Зеленый']

    def running(self):
        for i in TrafficLight.__color:
            print(i)
            if i == 'Красный':
                sleep(7)
            elif i == 'Жёлтый':
                sleep(2)
            elif i == 'Зеленый':
                sleep(7)
        print('end')


trafficLight1 = TrafficLight()
trafficLight1.running()


# Задание №2


class Road:
    def __init__(self, length, width, mass=25, height=1):
        self._l = length
        self._w = width
        self._m = mass
        self._h = height

    def mass(self):
        result = self._l * self._w * self._m * self._h / 1000
        return print(f'{self._l}м. * {self._w}м. * {self._m}кг. * {self._h}см. = {int(result)}т.')


road1 = Road(20, 5000, height=5)
road1.mass()


# Задание №3


class Worker:
    _income = {
        'Слесарь': [40000, 10000],
        'Оператор': [50000, 10000],
        'Наладчик': [80000, 20000],
        'Мастер': [60000, 20000],
        'Директор': [100000, 50000]
    }

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        if self.position in Worker._income:
            a = [Worker._income[p][0] + Worker._income[p][1] for p in Worker._income if p == self.position]
            return f'Доход составляет: {a[0]}р.'
        else:
            return f'Позицией могут быть только {Worker._income.keys()}'


fixer1 = Position('Дмитрий', 'Миронов', 'Наладчик')
print(fixer1.get_full_name())
print(fixer1.get_total_income())


# Задание №4


class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return print(f'{self.name} движется вперёд')

    def stop(self):
        return print(f'{self.name} остановился')

    def turn(self, direction):
        a = ['Налево', 'Направо']
        if direction in a:
            return print(f'{self.name} повернул {direction}')
        else:
            return print(f'Автомобиль может поворачивать только "Налево" или "Направо".')

    def show_speed(self):
        return print(f'{self.name} движется со скоростью: {self.speed}км/ч.')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return print(f'Скорость автомобиля {self.speed}км/ч. Снизте скорость до 60км/ч!')
        else:
            return print(f'Скорость автомобиля {self.speed}км/ч.')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return print(f'Скорость автомобиля {self.speed}км/ч. Снизте скорость до 40км/ч!')
        else:
            return print(f'Скорость автомобиля {self.speed}км/ч.')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


tc1 = TownCar(50, 'Чёрный', 'Nissan')
tc2 = TownCar(80, 'Серый', 'LADA')
tc1.go()
tc1.stop()
tc1.turn('Налево')
print(tc1.name)
tc1.show_speed()
print(tc2.name)
tc2.show_speed()
tc1.turn('Назад')
sc1 = SportCar(200, 'Красный', 'F1')
print(sc1.name, sc1.color, sc1.is_police)
wc1 = WorkCar(50, 'Белый', 'Ford')
wc1.show_speed()
pc1 = PoliceCar(90, 'Белый', 'Skoda')
print(pc1.name, pc1.color, pc1.is_police)
pc1.turn('Направо')


# Задание №5


class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Отрисовка как у {self.title}'


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Отрисовка как у ручки'


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Отрисовка как у карандаша'


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Отрисовка как у маркера'


pen1 = Pen('Ручка')
print(pen1.draw())
pencil1 = Pencil('Карандаш')
print(pencil1.draw())
handle1 = Handle('Маркер')
print(handle1.draw())