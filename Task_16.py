# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в списке A[1..N]. Пользователь в первой
# строке вводит натуральное число N – количество элементов в списке.В последующих строках записаны N целых чисел Ai.
# Последняя строка содержит число X

from random import randint

# # solution according to the condition
# qnt = int(input('Input N: '))
#
# listik = []
#
# for i in range(1, qnt + 1):
#     listik.append(randint(1, 10))
# print(listik)
#
# num = int(input('Input the number X: '))
#
# print(listik.count(num))


## another solution (using list comprehension)

li = [randint(1, 5) for i in range(1, int(input('Input the qnt of nums: ')) + 1)]
print(li)
print(li.count(int(input('Input a number btw 1 and 5: '))))
