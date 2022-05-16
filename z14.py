# Подсчитать сумму цифр в вещественном числе.
# N = float(input("введите число: "))
# while N % 10 != 0:
#     N = N * 10   # N = round(N * 10, 3)
# N = N // 10
# print(N)


# N = str(input("Введите число: "))
# sum = 0
# list = []
# for i in N:
#     if i != '.':
#         list.append(i)
# int_lst = [int(j) for j in list]
# for i in int_lst:
#     sum += i
# print(sum)


# def sum_of_digits(num):
#     sum = 0
#     while num > 0:
#         sum += num % 10
#         num //= 10
#     return sum
# N = int(input('введите число '))
# print(sum_of_digits(N))

N = str(input("Введите число: "))
if N.isnumeric():
    print("значение не является вещественным числом")
else:
    sum = 0
    number = list(N)
    number.remove('.')
    for i in number:
     sum += int(i)
print(sum)
