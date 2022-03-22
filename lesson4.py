# Задание №1


# from sys import argv
#
#
# def zp(hours=argv[1], income=argv[2], bonus=argv[3]):
#     try:
#         res = int(hours) * int(income) + int(bonus)
#     except ValueError:
#         print('Параметры должны быть числами')
#     else:
#         print(f'заработная плата сотрудника составит {res}')
#
#
# zp()

# Задание №2


# my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# res = [my_list[i] for i in range(1, len(my_list)) if my_list[i] > my_list[i - 1]]
# print(my_list)
# print(res)

# Задание №3


# print([el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0])

# Задание №4


# my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# res = [el for el in my_list if my_list.count(el) < 2]
# print(my_list)
# print(res)

# Задание №5


# from functools import reduce
#
#
# def my_func(arg1, arg2):
#     return arg1 * arg2
#
#
# print(reduce(my_func, [i for i in range(100, 1001, 2)]))


# Задание №6,1

# from itertools import count
#
# try:
#     for el in count(int(input('Введите стартовое число: '))):
#         if el == 100:
#             print(el)
#             break
#         elif el > 100:
#             print('Число должно быть меньше 100')
#             break
#         print(el)
# except ValueError:
#     print('Введите число')

# Задание №6,2


# from itertools import cycle
#
# my_list = [12, [1,'qwe'], 'rty', True]
# for i, el in enumerate(cycle(my_list)):
#     if i == 25:
#         break
#     print(el)


# Задание №7

# from math import factorial
#
#
# def fact(n):
#     for el in (factorial(i) for i in range(1, n + 1)):
#         yield el
#
#
# for el in fact(7):
#     print(el)
