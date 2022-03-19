# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]
N = int(input("Введите число: "))
list = []
product_of_numbers = 1
for i in range(1, N+1):
    product_of_numbers = product_of_numbers * i
    list.append(product_of_numbers)
print(list)

