import os
os.system('cls')

# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

# size = int(input('Введите кол-во эллементов в массиве: '))
# my_list = list()
# for i in range(size):
#     # my_list.append(i+1)
#     my_list.append(int(input(f'Введите {i+1}-е значение: ')))

# print(my_list)
# need_num = int(input('Введите проверочное число: '))
# count = 0
# for i in range(len(my_list)):
#     if my_list[i] == need_num:
#         count += 1
# print(f'Число {need_num} встречается в списке: {count}-раз\а')



# --------------------------------------------------------------------------------------------------------------------------------------------------------
# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

# N = int(input('Длинна массива:'))
# # a = [int(input('Ввести число:')) for i in range(N)]
# a = list()
# for i in range(N):
#     # my_list.append(i+1)
#     a.append(int(input(f'Введите {i+1}-е значение: ')))
# x = int(input('Заданное число:'))

# minraz = (x - a[0])**2 # Минимальная разница по модулю (для сравнения первый элемент)

# b = 0 # Нулевой индекс a[i]
# i = 0 # Начальная переменная для цикла

# while i < len(a):
#         if a[i] == x:
#                 print(x)
                
#         if (x-a[i])**2 <= minraz:
#                 minraz = (x-a[i])**2
#                 b = i
#                 i += 1
# print('Последовательность: ', a)
# print('Самое близкое значение элемента массива: ', a[b])
# print('Индекс элемента массива: ', b)






# --------------------------------------------------------------------------------------------------------------------------------------------------------
# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются
# так:
# A, E, I, O, U, L, N, S, T, R – 1 очко; 
# D, G – 2 очка; 
# B, C, M, P – 3 очка; 
# F, H, V, W, Y – 4 очка; 
# K – 5 очков; 
# J, X – 8 очков; 
# Q, Z – 10 очков.
# А русские буквы оцениваются так: 
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
# *Пример:*
# ноутбук
#     12
# test

eng = 'qwertyuiopasdfghjklzxcvbnm'
rus = 'йцукенгшщзхъфывапролджэячсмитьбюё'
eng_words = {1:'AEIOULNSTR', 2:'DG', 3:'BCMP', 4:'FHVWY', 5:'K', 8:'JX', 10:'QZ'}
ru_words = {1:'АВЕИНОРСТ', 2:'ДКЛМПУ', 3:'БГЁЬЯ', 4:'ЙЫ', 5:'ЖЗХЦЧ', 8:'ШЭЮ', 10:'ФШЪ'}
text = input('Ввведите слово: ').upper()

if text[0].lower() in eng:
        result = 0
        for i in text:
                for k, v in eng_words.items():
                        if i in v:
                                result += k   
        print(result)
else:
        result = 0
        for i in text:
                for k, v in ru_words.items():
                        if i in v:
                                result += k   
        print(result)






