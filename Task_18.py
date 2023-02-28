# # Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в
# # первой строке вводит натуральное число N – количество элементов в массиве. В последующих строках записаны N целых
# # чисел Ai. Последняя строка содержит число X
from random import randint

li = [randint(1, 6) for i in range(1, int(input('Input the qnt of nums: ')) + 1)]
print(*li)

user_num = int(input('Input the X number: '))
num_min = 2147483647
interval = 2147483647

for i in li:
    if i == user_num:
        num_min = i
        break
    if abs(user_num - i) == abs(interval):
        if num_min > i:
            num_min = i
            interval = user_num - i
    if abs(user_num - i) < abs(interval):
        num_min = i
        interval = user_num - i

print(f'The nearest number is: {num_min}')