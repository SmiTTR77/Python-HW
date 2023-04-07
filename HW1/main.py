# Урок 1. Ввод-Вывод, операторы ветвления

# Задача 2: Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

# n = str(input('введите трехзначное число: '))
# if len(n) != 3:
#     print('Введите число состоящее из трех знаков!')
# else:
#     sum = 0
#     for i in n:
#         sum += int(i)
#     print(f'Сумма цифр числа {n} равна {sum}')


# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# Пример:
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

# s = int(input('Введите общее количество журавликов: '))
# if s % 2 == 0:
#     n = s // 6
#     print(f'Петя сделал {n}, Катя {4*n}, Сережа {n}')
# else:
#     print('По условию задачи ребята не могли сделать нечетное количество журавликов')

# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5 = 9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# Пример:
# 385916 -> yes
# 123456 -> no

# ticket = str(input('Введите номер билета: '))
# if len(ticket) != 6:
#     print('Введите шесть цифр номера билета!')
# else:
#     halfA = str(ticket[:3])
#     halfB = str(ticket[-3:])
#     sumA = 0
#     for i in halfA:
#         sumA += int(i)
#     sumB = 0
#     for i in halfB:
#         sumB += int(i)

#     if sumA == sumB:
#         print('yes')
#     else:
#         print('no')


# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками(то есть разломить шоколадку на два прямоугольника).
# Пример:
# 3 2 4 -> yes
# 3 2 1 -> no

sideN = int(input('Введите сторону шоколадки n: '))
sideM = int(input('Введите сторону шоколадки m: '))
slice = int(input('Введите количество долек: '))

if slice >= sideN * sideM or slice == 0:
    print('no')
elif slice % sideN == 0 or slice % sideM == 0:
    print('yes')
else:
    print('no')
