# Найти сумму чисел списка стоящих на нечетной позиции
list = [1, 2, 3, 4, 5, 6, 7]
sum = 0
for i in range(len(list)):
    if i% 2 !=0:
     sum = sum + list[i]
print(sum)