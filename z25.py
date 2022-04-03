# Написать программу преобразования десятичного числа в двоичное
n = int(input("введите число: "))
b = ''
while n > 0:
    b = str(n % 2) + b
    print(f'b= {b}')
    n = n // 2
    print(f'n= {n}')
print(b)
# n = int(input("введите число: "))
# print(bin(n))

# print(int(5%2))