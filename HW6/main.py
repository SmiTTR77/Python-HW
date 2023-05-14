# Task 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

import random

my_list = []

value_a1 = int(input('Введите первый элемент: '))
value_d = int(input('Введите разность: '))
value_n = int(input('Введите количество элементов: '))

for i in range(value_n):
    value_an = value_a1 + i * value_d
    my_list.append(value_an)
    print(value_an)
print(my_list)


# Task 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

size = int(input('Введите размер списка: '))
min_value = int(input('Введите минимальное значение списка: '))
max_value = int(input('Введите максимальное значение списка: '))

my_list = [random.randint(min_value, max_value) for _ in range(size)]
print(my_list)

min_range = int(input('Введите минимальное значение диапозона: '))
max_range = int(input('Введите максимальное значение диапозона: '))

for i in range(len(my_list)):
    if min_range <= my_list[i] <= max_range:
        print(i)
