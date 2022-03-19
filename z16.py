# Задать список из n чисел последовательности (1+1/n)**n и вывести на экран их сумму
N = int(input("Введите число: "))
list = []
A = 0
sum = 0
for i in range(1, N+1):
    A = (1+1/i)**i
    list.append(A)
print(list)
for i in list:
 sum = sum + i
print(sum)
