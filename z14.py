# Подсчитать сумму цифр в вещественном числе.
N = float(input("введите число: "))
while N % 10 != 0:
    N = N * 10
N = N // 10
print(N)

def sum_of_digits(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    return sum

print(sum_of_digits(N))