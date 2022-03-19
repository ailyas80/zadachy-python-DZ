# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]
N = input("Введите число: ")
list = []
product_of_numbers = 1
for i in N:
    list.append(product_of_numbers * i)
print(list)

