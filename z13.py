# Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.

def text1(s1, s2):
    count = 0
    i = -1
    while True:
        i = s1.find(s2, i+1)
        if i == -1:
            return count
        count += 1

print(text1('abababa ', 'c'))
