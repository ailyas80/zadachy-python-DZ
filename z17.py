# Задать список из N элементов, заполненных числами из [-N, N].
# Найти произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число

list = []
with open('D:/z17.txt', 'r') as file:
 line = file.readline()
 while line:
     print(line, end="")
     line = file.readline()
     list.append(line)
print(list)



# print(list)
# print(list)

# print(data)

# file = open('D:/z17.txt', 'r')
# sum = 0
# for i in file:
#     sum = sum + i
#     print(sum)

