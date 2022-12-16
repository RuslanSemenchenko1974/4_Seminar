
def function():
    while True:
        try:
            x = int(input("Введите число : "))
        except ValueError:
            print("Error! Это не число, попробуйте снова.")
        else:
            return x


def fibonacci_1(n):
    if n == 1:
        return 1
    if n == 2:
        return -1
    else:
        return -fibonacci_1(n - 1) + fibonacci(n - 2)


us_namber = function()
print(f'{us_namber} : {fibonacci_1(us_namber)}')
for i in range(us_namber):
    print(fibonacci_1(us_namber - i))