import numpy as np


def seidel_method(A, b, x0=None, tol=1e-6, max_iter=1000):
    """
    Метод Зейделя для решения СЛАУ
    
    Параметры:
    A - матрица коэффициентов системы
    b - вектор правых частей
    x0 - начальное приближение
    tol - допустимая погрешность
    max_iter - максимальное количество итераций
    
    Возвращает:
    x - вектор решения
    iterations - количество выполненных итераций
    """
    n = len(A)
    
    if x0 is None:
        x = np.zeros(n)
    else:
        x = x0.copy()
    
    for iteration in range(max_iter):
        x_new = x.copy()
        
        for i in range(n):
            sum1 = np.dot(A[i, :i], x_new[:i])
            sum2 = np.dot(A[i, i+1:], x[i+1:])
            x_new[i] = (b[i] - sum1 - sum2) / A[i, i]
        
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


x, iterations = seidel_method(A, b)
print("Решение системы:")
print(x)
print(f"\nКоличество итераций: {iterations}")
