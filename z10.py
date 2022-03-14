# Найти расстояние между двумя точками пространства
from turtle import distance


x1 = int(input("введите первую координату x1 "))
y1 = int(input("введите первую координату y1 "))
x2 = int(input("введите вторую координату x2 "))
y2 = int(input("введите вторую координату y2 "))
distance = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
print(round(distance,2))
