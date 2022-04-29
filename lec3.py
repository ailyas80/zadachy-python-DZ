str_fib = ['1','2']
print(type(str_fib))
# int_fib = [int(k) for k in str_fib]
# print(int_fib)

# data = '1 2 3 5 8 15 23 38'.split()
# res = map(int, data)
# res = filter(lambda x: not x%2, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)


users = ['user1', 'user2', 'user3', 'user4', 'user5']
data = list(enumerate(users))
print(data)









# def f(x):
#     return x**2
# with open('file22.txt', 'r') as file2:
#     data2 = file2.read()
#     data2 = list(map(int,(data2.split())))
# file2.close()
# list = [(i, f(i)) for i in data2 if i % 2 == 0]
# print(list)
