""" Реализовать скрипт, в котором должна быть предусмотрена функция расчета
заработной платы сотрудника. В расчете необходимо использовать формулу: 
(выработка в часах*ставка в час) + премия. Для выполнения расчета для 
конкретных значений необходимо запускать скрипт с параметрами."""
from sys import argv

script_name, w_time, h_salary, m_prize = argv


def function():
    while True:
        try:
            x = int(input())
        except ValueError:
            print("Error! Это не число, попробуйте снова.")
        else:
            return x


def salary(work_time, hour_salary, prize):
    return work_time * hour_salary + prize


"""print('Введите отработанное сотрудником время : ')
w_time = function()
print('Введите з/п сотрудника в час  :')
h_salary = function()
print('Введите премию : ')
m_prize = function()"""
print(script_name)
w_time = int(w_time)
h_salary = int(h_salary)
m_prize = int(m_prize)
print(f'Заработная плат сотрудника : {salary(w_time, h_salary, m_prize)}')


