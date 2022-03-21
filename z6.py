# Дано число обозначающее день недели.
# Вывести его название и указать является ли он выходным.
def weekend(some_number):
    return some_number == 5 or some_number == 6


number = int(input("введите число от 0 до 6: "))
weekdays = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
if weekend(number) == True:
    print(weekdays[number], '- Выходной день')
else:
    print(weekdays[number], '- рабочий день')
