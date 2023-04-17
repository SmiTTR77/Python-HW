# Task 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..size]. 
# Пользователь в первой строке вводит натуральное число size – количество элементов в массиве. 
# В последующих  строках записаны size целых чисел Ai. Последняя строка содержит число X
# Пример:
# 5
#     1 2 3 4 5
#     3
#     -> 1

# import random

# size = int(input('Введите размер списка: '))
# my_list = [random.randint (0,10) for i in range (size)]
# print (my_list)

# num = int(input('Введите искомое число: '))
# count = 0

# for i in my_list:
#     if i == num:
#         count += 1
        
# print(f'Ваше число встречается {count} раз(а)')


# Task 18: Требуется найти в массиве A[1..size] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число size – количество элементов в массиве. 
# В последующих  строках записаны size целых чисел Ai. Последняя строка содержит число X
# Пример:
# 5
#     1 2 3 4 5
#     6
#     -> 5

# import random

# size = int(input('Введите размер списка: '))
# my_list = [random.randint(1, 10) for i in range(size)]
# print(my_list)

# num = int(input('Введите искомое число: '))
# index_value = 0
# min_value = abs(my_list[0] - num)

# for i in range(1, size):
#     temp_value = abs(my_list[i] - num)

#     if temp_value < min_value:
#         min_value = temp_value
#         index_value = i

# print(f'Ближайший по величине элемент к числу "{num}" является число "{my_list[index_value]}"')

# Task 16+18

import random

size = int(input('Введите размер списка: '))
my_list = [random.randint(1, 10) for i in range(size)]
print(my_list)

num = int(input('Введите искомое число: '))
count = 0
index_value = 0
min_value = abs(my_list[0] - num)

for i in my_list:
    if i == num:
        count += 1        
print(f'Ваше число встречается {count} раз(а)')

for i in range(1, size):
    temp_value = abs(my_list[i] - num)
    if temp_value < min_value:
        min_value = temp_value
        index_value = i
print(f'Ближайший по величине элемент к числу "{num}" является число "{my_list[index_value]}"')


# Task 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:
#     A, E, I, O, U, L, size, S, T, R – 1 очко; 
#     D, G – 2 очка; B, C, M, P – 3 очка; 
#     F, H, V, W, Y – 4 очка; K – 5 очков; 
#     J, X – 8 очков; Q, Z – 10 очков. 
# А русские буквы оцениваются так: 
#     А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
#     Д, К, Л, М, П, У – 2 очка; 
#     Б, Г, Ё, Ь, Я – 3 очка; 
#     Й, Ы – 4 очка; 
#     Ж, З, Х, Ц, Ч – 5 очков; 
#     Ш, Э, Ю – 8 очков; 
#     Ф, Щ, Ъ – 10 очков. 
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
# Пример:
# ноутбук
#     12

# my_word = input('Введите слово: ').upper()
# print(my_word)
# # print(type(my_word))

# score = 0

# # for i in my_word:
# #     print(i)

# for i in my_word:
# 	if i == "А" or "В" or "Е" or "И" or "Н" or "О" or "Р" or "С" or "Т":
# 		score += 1
# 		print(i, score)
# 	elif i == "Д" or "К" or "Л" or "М" or "П" or "У":
# 		score += 2
# 	elif i == "Б" or "Г" or  "Ё" or "Ь" or "Я":
# 		score += 3		
# 		print(i, score)
# 	elif i == "Й" or "Ы":
# 		score += 4
# 	elif i == "Ж" or "З" or "Х" or "Ц" or "Ч":
# 		score += 5
# 	elif i == "Ш" or "Э" or "Ю":
# 		score += 8
# 	elif i == "Ф" or "Щ" or "Ъ":
# 		score += 10
# 	else:
# 		print('wtf')
  
# print(f'Вы набрали {score} очка(ов)')


# Dictionary worked version
points_table = {1:"AEIOULNSTRАВЕИНОРСТ",2:"DGДКЛМПУ",3:"BCMPБГЁЬЯ",4:"FHVWYЙЫ",5:"KЖЗХЦЧ",8:"JXШЭЮ",10:"QZФЩЪ"}

my_word = input("Введите слово: ").upper()
score = 0

for i in my_word:
    for point, value in points_table.items():
        if i in value:
            score += point
            
print(f'Вы набрали {score} очка(ов)')