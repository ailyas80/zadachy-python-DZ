def negafib(n): 
    if n in [-1,0,1]: 
        return abs(n) 
    elif n < 0: 
        n = abs(n) 
        return (-1)**(n+1)*(negafib(n-1)+negafib(n-2)) 
    else: 
        return negafib(n-1)+negafib(n-2) 

 
n = int(input('Введите число n = ')) 
list = [] 
print(negafib(n))
for i in range(-n,n+1): 
    list.append(negafib(i)) 
print(list)

