"""
def split1(line, types=None, delimiter=None):
     Разбивает текстовую строку и при необходимости
    выполняет преобразование типов.
    ...

    fields = line.split(delimiter)
    if types:
        fields = [ty(val) for ty, val in zip(types, fields)]
    return fields


employee_numbers = [2, 9, 18, 28]
employee_names = ["Дима", "Марина", "Андрей", "Никита"]

zipped_values = zip(employee_names, employee_numbers)
print(zipped_values)
zipped_list = list(zipped_values)

print(zipped_list)

print(split1('0 1 2', [int, int, int]))


def func(x):
    x = x * x
    #print(x)
    return x


mylist = [5, 5, 5]
list2 = list(map(func, mylist))
print(list2)

employee_numbers = [2, 9, 18, 28]
employee_names = ["Дима", "Марина", "Андрей", "Никита"]

for name, number in zip(employee_names, employee_numbers):
	print(name, number)
print (list(zip(employee_names, employee_numbers)))
employees_zipped = [('Дима', 2), ('Марина', 9), ('Андрей', 18), ('Никита', 28)]
employee_names, employee_numbers = zip(*employees_zipped)

print(employee_names)
print(employee_numbers)
"""
print(15//2)