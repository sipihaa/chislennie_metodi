import numpy as np


def secant_method(f, x0, x1, tol=1e-6, max_iter=100):
    """
    Метод секущих для решения нелинейных уравнений
    
    Параметры:
    f - функция, для которой ищем корень
    x0, x1 - начальные приближения
    tol - допустимая погрешность
    max_iter - максимальное количество итераций
    
    Возвращает:
    x - найденный корень
    iterations - количество итераций
    """
    iterations = 0
    
    while iterations < max_iter:
        fx0 = f(x0)
        fx1 = f(x1)
        
        if abs(fx1) < tol:
            return x1, iterations
            
        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        
        x0, x1 = x1, x2
        iterations += 1
        
    raise Exception("Метод не сошелся за максимальное число итераций")


def f(x):
    return x**3 + x**2 - 4

x0 = 1.0
x1 = 3.0

root, iters = secant_method(f, x0, x1)
print(f"Найденный корень: {root}")
print(f"Количество итераций: {iters}")
print(f"Значение функции в корне: {f(root)}")
