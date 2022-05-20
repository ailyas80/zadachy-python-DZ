# Строка содержит набор чисел. Показать большее и меньшее число
# Символ-разделитель - пробел
x = '1 2 3 4 5 6 7'
x = list(map(int,(x.split())))
print(f'{max(x)}: {min(x)}')

# x = [int(input("введите числа  ")) for i in range(1, 4)]
# print(type(x))
# print(x)