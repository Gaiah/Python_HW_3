#3 #Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
import math

list =  [1.7, 1.2, 3.1, 5.3, 10.01]

min_elem = math.inf
max_elem = - math.inf

for i in range(len(list)):
    if list[i] % 1 < min_elem:
        min_elem = list[i] % 1
    elif list[i] % 1 > max_elem:
        max_elem = list[i] % 1
print(f'{round(max_elem, 3)} - {round(min_elem, 3)} = {round(max_elem - min_elem, 3)}')