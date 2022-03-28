# Задание №1


with open(r'tasks\task1.txt', 'w', encoding='utf-8') as t:
    while True:
        line = input('Введите текст или ничего для выхода: ') + '\n'
        if line == '\n':
            break
        t.writelines(line)

# Задание №2


with open(r'tasks\task2.txt', 'r', encoding='utf-8') as t:
    print(t)
    lines = t.readlines()
    print(f'Количество строк в файле: {len(lines)}')
    t.seek(0)
    words = t.read()
    word = words.split()
    print(f'Количество слов: {len(word)}')

# Задание №3


from functools import reduce

with open(r'tasks\task3.txt', 'r', encoding='utf-8') as t:
    workers = t.read().split('\n')
    my_dict = {}
    for i in workers:
        worker = i.split()
        my_dict[worker[0]] = float(worker[1])
    print(f'Зарплата ниже 20000 у: {[i for i in my_dict if my_dict[i] <= 20000]}')


    def summa(x, y):
        return x + y


    print(f'Средняя величина дохода сотрудников: {reduce(summa, [my_dict[i] for i in my_dict]) / len(my_dict)} р.')

# Задание №4


new_list = []
with open(r'tasks\task4_1.txt', 'r', encoding='utf-8') as t:
    my_list = t.readlines()
    my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    for i in my_list:
        words = i.split()
        for word in words:
            new_list.append(my_dict[word]) if word in my_dict else new_list.append(' ' + word)
        new_list.append('\n')

with open(r'tasks\task4_2.txt', 'w', encoding='utf-8') as tn:
    tn.writelines(new_list)

# Задание №5


with open(r'tasks\task5.txt', 'w+', encoding='utf-8') as t:
    my_list = input('Введите цифры через пробел: ')
    t.writelines(my_list)
    t.seek(0)
    numbers = t.read().split()
    summa = 0
    for number in numbers:
        try:
            summa = summa + int(number)
        except ValueError:
            print(f"'{number}' не является числом")
    print(f'Сумма чисел в файле равна: {summa}')

# Задание №6


with open(r'tasks\task6.txt', 'r', encoding='utf-8') as t:
    subjects = t.readlines()
    my_dict = {}
    for subject in subjects:
        my_list = subject.split()
        res = 0
        for i in range(1, 4):
            x = ''
            try:
                for n in my_list[i]:
                    if 48 <= ord(n) <= 57:
                        x = x + n
            except:
                continue
            if not x:
                continue
            else:
                res = res + int(x)
        my_dict[my_list[0][0:-1]] = res
    print(my_dict)

# Задание №6


import json

my_result_list = []
with open(r'tasks\task7.txt', 'r', encoding='utf-8') as t:
    farms = t.readlines()
    profit_dict = {}
    un_profit_dict = {}
    average_dict = {'average_profit': 0}
    for farm in farms:
        my_list = farm.split()
        sal = int(my_list[2]) - int(my_list[3])
        if sal >= 0:
            profit_dict[my_list[0]] = sal
        else:
            un_profit_dict[my_list[0]] = sal
        average_dict['average_profit'] = average_dict['average_profit'] + sal
    average_dict['average_profit'] = average_dict['average_profit'] / len(farms)
    my_result_list.append(profit_dict), my_result_list.append(un_profit_dict), my_result_list.append(average_dict)
print(my_result_list)

with open(r'tasks\task7j.json', 'w') as tj:
    json.dump(my_result_list, tj)
    result = json.dumps(my_result_list)
    print(f'Создан файл task7j.json:\n {result}')
