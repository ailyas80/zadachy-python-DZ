# Для натурального n создать словарь индекс-значение,
# состоящий из элементов последовательности 3n + 1. 
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
N = int(input("введите N:"))
index = []
slovar = []
for i in range(1, N+1):
    index.append(i)
    slovar.append(3*i + 1)
print('{', end="")
for i in range(N):
    print(f'{index[i]}: {slovar[i]}', end="")
    if i < N-1:
     print(', ', end="")
print('}')
