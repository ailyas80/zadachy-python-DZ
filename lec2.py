# colors = ['red', 'green', 'blue']
# data = open('filelec2.txt', 'a')
# data.writelines(colors)
# data.write('\nLINE \n')
# data.write('LINE3\n')
# data.close()


# with open('filelec2.txt', 'a') as data:
#     data.write('\nLINE333 \n')
#     data.write('LINE3555\n')


# path = 'filelec2.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()


# import hello as h

# print(h.f(1))


# def new_string(symbol, count = 3):
#     return symbol * count
# print(new_string('!', 5))
# print(new_string('!'))
# print(new_string(4))




# def concatenatio(*params):
#     res: str = ""
#     for item in params:
#         res += item     # res = res + item
#     return res

# print(concatenatio('a', 's', 'd', 'w'))  # asdw
# print(concatenatio('a', '1'))    # a1




# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

# list = []
# for e in range(1, 10):
#     list.append(fib(e))
# print(list)


# a = (3, 4, 5)
# print(a)
# print(a[0])

# for item in a:
#     print(item)


# t = tuple(['red', 'green', 'blue'])
# red, green, blue = t

# print('r:{} g:{} b:{}'.format(red, green, blue))



# dictionary = {}
# dictionary = \
#     {
#         'up': '↑',
#         'left': '←',
#         'down': '↓',
#         'right': '→'
#     }
# # print(dictionary)
# # print(dictionary['left'])

# for k in dictionary.keys():
#     print(k)


# colors = {'green', 'blue'}
# print(colors)
# colors.discard('red')
# print(colors)
# colors.add('red')
# print(colors)


# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() 
# u = a.union(b)
# i = a.intersection(b)
# dl = a.difference(b)
# dr = b.difference(a)

# q = a \
#     .union(b) \
#     .difference(a.intersection(b))   # это тоже самое = a.union(b).difference(a.intersection(b))
# print(q)



# s = frozenset(a) # заморозка массива

