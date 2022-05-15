# Дано число обозначающее день недели.
# Вывести его название и указать является ли он выходным.
def weekend(some_number):
    weekdays = ['Понедельник', 'Вторник', 'Среда',
                'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    if some_number <= 0 or some_number >= 8:
        return 'не корректный ввод'
    if some_number == 6 or some_number == 7:
     return weekdays[some_number-1] + ' Выходной день'
    else:
        return weekdays[some_number-1] + ' Рабочий день'

N = int(input('Введите день недели: '))
print(weekend(N))