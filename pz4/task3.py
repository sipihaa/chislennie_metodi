import numpy as np


def gauss_rectangle_rule(A, b):
    """
    Метод Гаусса с использованием правила прямоугольника
    
    Параметры:
    A - матрица коэффициентов системы
    b - вектор правых частей
    
    Возвращает:
    x - вектор решения
    """
    n = len(A)
    Ab = np.column_stack((A, b))
    
    for k in range(n):
        if abs(Ab[k, k]) < 1e-10:
            raise ValueError("Матрица вырождена")
        
        for i in range(k + 1, n):
            for j in range(k + 1, n + 1):
                Ab[i, j] = Ab[i, j] - (Ab[i, k] * Ab[k, j]) / Ab[k, k]
            Ab[i, k] = 0
    
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (Ab[i, -1] - np.dot(Ab[i, i+1:n], x[i+1:])) / Ab[i, i]
    
    return x


A = np.array([
    [2.0, 1.0, -1.0],
    [-3.0, -1.0, 2.0],
    [-2.0, 1.0, 2.0]
], dtype=float)

b = np.array([8.0, -11.0, -3.0], dtype=float)

x = gauss_rectangle_rule(A, b)
print("Решение системы:")
print(x)
