import numpy as np


def simple_iteration(A, b, x0=None, tol=1e-6, max_iter=1000):
    """
    Метод простых итераций для решения СЛАУ
    
    Параметры:
    A - матрица коэффициентов системы
    b - вектор правых частей
    x0 - начальное приближение (если None, то используется нулевой вектор)
    tol - допустимая погрешность
    max_iter - максимальное количество итераций
    
    Возвращает:
    x - вектор решения
    iterations - количество выполненных итераций
    """
    n = len(A)
    
    B = np.zeros((n, n))
    c = np.zeros(n)
    
    for i in range(n):
        for j in range(n):
            if i != j:
                B[i, j] = -A[i, j] / A[i, i]
        c[i] = b[i] / A[i, i]
    
    if x0 is None:
        x = np.zeros(n)
    else:
        x = x0.copy()
    
    for iteration in range(max_iter):
        x_new = np.dot(B, x) + c
        
        if np.all(np.abs(x_new - x) < tol):
            return x_new, iteration + 1
        
        x = x_new
    
    raise Exception("Метод не сошелся за максимальное число итераций")


A = np.array([
    [10.0, 1.0, 1.0],
    [1.0, 10.0, 1.0],
    [1.0, 1.0, 10.0]
], dtype=float)

b = np.array([12.0, 12.0, 12.0], dtype=float)


x, iterations = simple_iteration(A, b)
print("Решение системы:")
print(x)
print(f"\nКоличество итераций: {iterations}")
