import os 
os.system('cls')
# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def arifm():
    n_start,n_step, n_count = map(int,input('Введите через пробел начало, шаг и размер соответственно->').split())
    my_list =[]
    n_end = n_start + (n_count - 1) * n_step
    for i in range(n_start, n_end + 1, n_step):
        my_list.append(i)
    return my_list
print(arifm())

#Динамический вариант:
# a1 = int(input())
# d = int(input())
# n = int(input())
# for i in range(n):
#     print(a1 + i * d)


# Задача 32: Определить индексы элементов массива(списка),
# значения которых принадлежат заданному диапазону(т.е. не меньше заданного минимума и не больше заданного максимума)
#диапазон от 1 ~ 14
import random
size = int(input('Введите размер массива: '))
list_0 = []
for i in range(size):
    list_0.append(random.randint(0, 51))
print('Исходный массив: ', list_0)
list_1 = []
list_res = []
a,b = map(int,input('Введите диапазон поиска значений: ').split())
for i in range(a, b +1):
    list_1.append(i)
for i in range(len(list_0)):
    if list_0[i] in list_1:
        list_res.append(i)
print(list_res)



# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_number = int(input())
# max_number = int(input())
# for i in range(len(list_1)):
#     if min_number <= list_1[i] <= max_number:
#         print(i)


