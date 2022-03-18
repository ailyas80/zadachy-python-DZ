# Подсчитать сумму цифр в вещественном числе.
# N = float(input("введите число: "))
# while N % 10 != 0:
#     N = N * 10   # N = round(N * 10, 3)
# N = N // 10
# print(N)
# str_lst = ['1', '2', '3']
# int_lst = [int(x) for x in str_lst]
# print (int_lst)

N = str(input("Введите число: "))
sum = 0
list = []
for i in N:
    if i != '.':
        list.append(i)
print(list)
int_lst = [int(x) for x in list]
print(int_lst[1])
for i in int_lst:
    sum = sum + i
print(sum)


# def sum_of_digits(num):
#     sum = 0
#     while num > 0:
#         sum += num % 10
#         num //= 10
#     return sum

# print(sum_of_digits(N))
