import numpy as np

def sum_proiz():
    mass = np.array([i for i in range(int(input('Введите число а: ')), int(input('Введите число b: ')))])
    proiz = 1
    proiz = [proiz * i for i in mass[mass < 0]]
    print(sum(mass[mass > 0]), proiz[0])

def null_col():
    matrix = np.array([
        [1, 0, 2],
        [0, 0, 3],
        [4, 0, 0],
        [0, 5, 6]
    ])
    zero_counts = np.sum(matrix == 0, axis=0)
    columns_with_more_than_two_zeros = np.where(zero_counts > 2)[0]
    print("Столбцы с более чем двумя нулевыми элементами:", columns_with_more_than_two_zeros[0])

sum_proiz()
null_col()