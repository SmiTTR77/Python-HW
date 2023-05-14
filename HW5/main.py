# Task 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

# Пример:
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def degree_num(num_a, num_b):
    if num_b == 0:
        return 1
    return num_a * degree_num(num_a, num_b - 1)


number_a = int(input('Введите число A: '))
number_b = int(input('Введите число B: '))

print(degree_num(number_a, number_b))

# Task 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# Пример:
# 	2 2
# 	4


def rec_sum(a, b):
    if b == 0:
        return a
    return rec_sum(a + 1, b - 1)


number_a = int(input('Введите целое неотрицательное число A: '))
number_b = int(input('Введите целое неотрицательное число B: '))

print(rec_sum(number_a, number_b))
