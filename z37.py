# Дан список чисел. Создать список в который попадают числа, описывающие 
# возрастающую последовательность и содержащие максимальное количество элементов. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
#         [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7]
#  Порядок элементов менять нельзя
list = [1, 5, 2, 3, 4, 6, 1, 7]
new_list = []
max = 0
# list = [(i, i) for i in list]
# print(list)
for i in list:
    if list[i] > max:
        max = list[i]
        print(max)
        new_list.append(max)
print(new_list)
