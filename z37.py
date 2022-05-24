# Дан список чисел. Создать список в который попадают числа, описывающие
# возрастающую последовательность и содержащие максимальное количество элементов.
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
#         [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7]
#  Порядок элементов менять нельзя
# list = [1, 5, 2, 3, 4, 6, 1, 7]
# new_list = []
# max = 0
# for i in list:
#     if i > max:
#         max = i
#         new_list.append(max)
# print(new_list)


# list = [1, 5, 2, 3, 4, 6, 1, 7]
# new_list = []
# maximum = max(list)
# for i in list:
#     if i > maximum:
#         # max = i
#         new_list.append(i)
# print(new_list)

X = [1, 5, 2, 3, 4, 6, 1, 7]
L = []
M = []
j = 1

while j < len(X):
    i = j
    N = X[:]
    while i < len(N)-1:
        if N[i] < N[i+1]:
            M.append(N[i])
            i += 1
        else:
            N.pop(i+1)
            print(M)
            print(N)

    j += 1
    if len(L) < len(M):
        L = M
    M = []

if X[-1] > L[-1]:
    L.append(X[-1])

if X[0] < L[0]:
    L.insert(0, X[0])

print(L)
