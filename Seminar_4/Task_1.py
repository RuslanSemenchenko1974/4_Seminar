""" Реализовать скрипт, в котором должна быть предусмотрена функция расчета
заработной платы сотрудника. В расчете необходимо использовать формулу: 
(выработка в часах*ставка в час) + премия. Для выполнения расчета для 
конкретных значений необходимо запускать скрипт с параметрами."""
from sys import argv

script_name, w_time, h_salary, m_prize = argv


def function(x):
    while True:
        try:
            x = int(x)
        except ValueError:
            print("Error! Это не число, попробуйте снова.")
        else:
            return x


def salary(work_time, hour_salary, prize):
    return work_time * hour_salary + prize



print(script_name)
w_time = function(w_time)
h_salary = function(h_salary)
m_prize = function(m_prize)
print(f'Заработная плат сотрудника : {salary(w_time, h_salary, m_prize)}')


