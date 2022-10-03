##.5 Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]
import math

user_n = abs(int(input("Input Fibonacci N: ")))
list_negative = []
list_positive = []

def fibonacci(n):
    if n == -1:
        return 1
    elif n == -2:
        return -1
    elif n in [1, 2]:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


for i in range(0, user_n + 1):
    list_negative.append(fibonacci(i) * ((-1)**(i+1)))
for k in list_negative[::-1]:
    print(k, end = "    ")

for i in range(1, user_n + 1):
    list_positive.append(fibonacci(i))
for j in list_positive:
    print(j, end = "    ")
