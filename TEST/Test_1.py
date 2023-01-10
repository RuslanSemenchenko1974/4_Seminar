from timeit import timeit


def c_test():
    my_list = []
    for i in range(10):
        my_list += [i]
    print(my_list)


print(timeit("x=2+2", number=1000))
print(timeit("x=sum(range(10))", number=1000))
print(timeit("c_test", globals=globals(), number=1000))
c_test()
g = []
g = [1, 2] + [2, 3]
print(g)
param = 123
str1 = "first {} ".format(param)
print(str1)
str1 = "first %s " % (param)
print(str1)
str1 = f"first {param}"
print(str1)