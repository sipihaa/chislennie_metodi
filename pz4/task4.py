import numpy as np


def lu_decomposition(A):
    """
    LU-разложение матрицы A
    
    Параметры:
    A - матрица коэффициентов системы
    
    Возвращает:
    L - нижняя треугольная матрица
    U - верхняя треугольная матрица
    """
    n = len(A)
    L = np.eye(n)
    U = A.copy()
    
    for k in range(n-1):
        for i in range(k+1, n):
            if U[k, k] == 0:
                raise ValueError("Матрица вырождена")
            L[i, k] = U[i, k] / U[k, k]
            for j in range(k, n):
                U[i, j] = U[i, j] - L[i, k] * U[k, j]
    
    return L, U


def solve_lu(L, U, b):
    """
    Решение системы Ax = b с использованием LU-разложения
    
    Параметры:
    L - нижняя треугольная матрица
    U - верхняя треугольная матрица
    b - вектор правых частей
    
    Возвращает:
    x - вектор решения
    """
    n = len(b)
    
    y = np.zeros(n)
    for i in range(n):
        y[i] = b[i] - np.dot(L[i, :i], y[:i])
    
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i+1:], x[i+1:])) / U[i, i]
    
    return x


def solve_system_lu(A, b):
    """
    Решение системы Ax = b методом LU-разложения
    
    Параметры:
    A - матрица коэффициентов системы
    b - вектор правых частей
    
    Возвращает:
    x - вектор решения
    """
    L, U = lu_decomposition(A)
    return solve_lu(L, U, b)


A = np.array([
    [2.0, 1.0, -1.0],
    [-3.0, -1.0, 2.0],
    [-2.0, 1.0, 2.0]
], dtype=float)

b = np.array([8.0, -11.0, -3.0], dtype=float)

x = solve_system_lu(A, b)
print("Решение системы:")
print(x)
