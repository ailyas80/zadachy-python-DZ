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


def fibonachi(n):
    fib1 = 0
    fib2 = 1
    fib = [fib1, fib2]
    i = 0
    while i < n - 2:
     fib_sum = fib1 + fib2
     fib1 = fib2
     fib2 = fib_sum
     fib.append(fib_sum)
     i += 1
    return fib

def antifib(n):
    fib1 = 1
    fib2 = -1
    fib = [fib1, fib2]
    i = 0
    while i < n - 3:
        fib_sum = fib1 - fib2
        fib1 = fib2
        fib2 = fib_sum
        fib.append(fib_sum)
        fib.reverse
        i += 1
    return fib

W = input("Введите число: ")
W = int(W)

print(antifib(W) + fibonachi(W))




# str_fib = [str(j) for j in fibonachi]
# print(str_fib)
# int_fib = [int(k) for k in str_fib]
# print(int_fib)
