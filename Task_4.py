# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
import math

list = [int(input("Input some number: "))]
li = []


for i in range(len(list)):
    while list[i] > 1:
        if list[i] % 2 == 1:
            li.append(1)
            list[i] = math.floor(list[i] / 2)
        elif list[i] % 2 == 0:
            li.append(0)
            list[i] = math.floor(list[i] / 2)            
    if list[i] == 1:
        li.append(1)
    else:
        li.append(0)

for j in li[::-1]:                              # for k in reversed(li):
    print(j, end = " ")                         #     print(k, end = " ")
