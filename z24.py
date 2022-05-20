# В заданном списке вещественных чисел найдите разницу между максимальным
# и минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
float_spisok = [1.1, 1.2, 3.1, 5, 10.01, 2.001]
new_float_spisok = []
for i in float_spisok:
    i = round(i - int(i), 10)
    if i !=0:
     new_float_spisok.append(i)
print(new_float_spisok)
print(f'{max(new_float_spisok)}- {min(new_float_spisok)} =  {max(new_float_spisok) - min(new_float_spisok)}')
