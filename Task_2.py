
# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
import math

list = [2, 3, 4, 5, 6]

count = math.ceil(len(list)/2)

product = 1
for i in range(len(list) + 1):
    if i == count:
        break
    else:
        product = list[i] * list[- i -1]
        print(f'{product} = {list[i]} * {list[-i -1]}')
