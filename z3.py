# Вывести на экран числа от -N до N
N = int(input('N = '))
list = []
x = N * (-1)
while x <= N:
    list.append(x)
    x += 1
print(list)
