"""Представлен список чисел. Определить элементы списка, не имеющие повторений.
 Сформировать итоговый массив чисел, соответствующих требованию. Элементы
 вывести в порядке их следования в исходном списке. Для выполнения задания
 обязательно использовать генератор."""

base_lst = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(base_lst)
generator = (base_lst[i] for i in range(0, len(base_lst))
             if base_lst.count(base_lst[i])==1)
res_lst=[]
for i in generator:
    res_lst.append(i)
print('Элементы списка, не имеющие повторений:')
print(res_lst)