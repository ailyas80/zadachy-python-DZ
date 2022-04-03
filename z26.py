# Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов. 
#  Т е для k = 8, список будет выглядеть так: 
#  [-21 ,13, -8, 5, −3,  2, −1,  1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# fib1 = fib2 = 1
# n = int(input("введите число: "))
# fibbonachi = []
# print(fib1, fib2, end=' ')
# for i in range(2, n):
#     fib1, fib2 = fib2, fib1 + fib2
#     print(fib2, end=' ')

# def fibonacci(n):
#     if n in (1, 2):
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)
 
# n = int(input("Введите число: "))
# print(fibonacci(n))

fib1 = 0
fib2 = 1
 
n = input("Введите число: ")
n = int(n)
fibonachi =[fib1, fib2]
i = 0
while i < n - 2:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    fibonachi.append(fib_sum)
    i += 1
print(fibonachi)