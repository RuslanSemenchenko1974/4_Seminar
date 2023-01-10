from random import randint


def create_matrix(n, m):
    matr = []

    for i in range(n):
        matr1 = []
        for j in range(m):
            matr1.append(randint(0, 10))
        matr.append(matr1)
    return matr


def mult_matrix(a, b):
    res_matrix = []

    _n = len(a[0])
    _m = len(b)
    _l = len(b[0])
    if _n == _m:
        for i in range(_l):
            h_matrix = []
            for j in range(_m):
                summ = 0
                for k in range(_n):
                    summ += a[i][k] * b[k][j]
                h_matrix.append(summ)
            res_matrix.append(h_matrix)
        return res_matrix
    else:
        print('!!!')

def print_my(matr):
    matr = '\n'.join(map(str, matr))
    return matr


"""создадим 2 матрицы """
a1 = create_matrix(5, 3)
print(print_my((a1)))
print('\n')
a2 = create_matrix(3, 5)
print(print_my((a2)))
print('\n')


print(print_my(mult_matrix(a1, a2)))
