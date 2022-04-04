# 43. Дана последовательность чисел. Получить список уникальных элементов 
# заданной последовательности. Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]
# list1 = [1, 2, 3, 5, 1, 5, 3, 10]
# list_unicum = []
# for i in list1:
#     if i not in list_unicum:
#         list_unicum.append(i)
#     else:
#         list_unicum.remove(i)
# print(list_unicum)

lst = [1, 2, 30, 3, 5, 11, 1, 5, 3, 10]
lst = [i for i in lst if lst.count(i) == 1] # lst.count(i) == 1 - количество вхождений элементов в списке равное одному
print(lst)