import numpy as np


def gauss_elimination(A, b):
    """
    Метод Гаусса (метод единственного деления) для решения СЛАУ
    
    Параметры:
    A - матрица коэффициентов системы
    b - вектор правых частей
    
    Возвращает:
    x - вектор решения
    """
    n = len(A)
    Ab = np.column_stack((A, b))
    
    for i in range(n):
        if abs(Ab[i, i]) < 1e-10:
            raise ValueError("Матрица вырождена")
            
        Ab[i] = Ab[i] / Ab[i, i]
        
        for j in range(i + 1, n):
            Ab[j] = Ab[j] - Ab[j, i] * Ab[i]
    
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = Ab[i, -1] - np.dot(Ab[i, i+1:n], x[i+1:])
    
    return x


A = np.array([
    [2.0, 1.0, -1.0],
    [-3.0, -1.0, 2.0],
    [-2.0, 1.0, 2.0]
], dtype=float)

b = np.array([8.0, -11.0, -3.0], dtype=float)

x = gauss_elimination(A, b)
print("Решение системы:")
print(x)
