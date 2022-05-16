# Показать первую цифру дробной части числа
N = float(input('N = '))
X = N * 10
X = X // 1
while X >= 10:
    X = round(X - 10)
print(X)

# def drob(N):
#     X = N * 10
#     X = X // 1
#     while X >= 10:
#         X = round(X - 10)
#     return X

# W = float(input('W = '))

# print(drob(W))
