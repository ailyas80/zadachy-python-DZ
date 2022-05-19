# Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.
Nstr = input("введите N:")
tmp = 1
list1 = []
list1.append(tmp)
if Nstr == '':
    print('некорректный ввод')
else:
    N = int(Nstr)
    for i in range(N-1):
        tmp *= -3
        list1.append(tmp)
print(f'N = {N}: {list1}')
