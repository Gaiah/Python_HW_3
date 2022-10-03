##.5 Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]
import math
import time

user_n = abs(int(input("Input Fibonacci N: ")))
list_negative = []
list_positive = []
start_time = time.time()
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
    list_negative.insert(0, fibonacci(i) * ((-1)**(i+1)))

for i in range(1, user_n + 1):
    list_negative.append(fibonacci(i))
for i in list_negative:
     print(i, end = "    ")
end_time = time.time()
print(end_time - start_time)
