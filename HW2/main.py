# Task 10: 
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

import random

coins_num = int(input('Введите количество монет: '))
coins = []
heads_side = 0
tails_side = 0

for i in range(coins_num):
	coins.append(random.randint(0, 1))
print(coins)

for i in coins:
	if coins[i] == 1:
		heads_side += 1
	else:
		tails_side += 1 
	print(heads_side, end = " ")
	print(tails_side)
print(f'Орлом выпало {heads_side}, решкой {tails_side}')

if heads_side > tails_side:
	print(f'Минимальное количество монет которое нужно перевернуть {tails_side}')
else:
	print(f'Минимальное количество монет которое нужно перевернуть {heads_side}')


# Task 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

# sum_x_y = int(input('Введите сумму чисел X и Y: '))
# prod_х_y = int(input('Введите произведение чисел X и Y: '))
# num_x = 0
# num_y = 0
# for i in range(sum_x_y):
# 	for j in range(prod_х_y):
# 		if sum_x_y == i + j and prod_х_y == i * j:  
# 			num_x = i
# 			num_y = j
# if num_x <= 1000 and num_y <= 1000:
#     print(f'Пятя задумал числа {num_x} и {num_y}')
# else:
#     print('Пятя задумал числа больше 1000')

   
# Task 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# num_n = int(input('Введите число N: '))
# degree_two = 2
# if num_n < 0:
#     print('Введите натуральное число')
# elif degree_two > num_n:
# 	print('Таких степеней числа 2 нет')
# else:
#     while degree_two < num_n:
#         print(degree_two)
#         degree_two *= 2
