import numpy as np


def newton_broyden(f, x0, tol=1e-6, max_iter=100):
    """
    Метод Ньютона-Бройдена
    
    Параметры:
    f - функция, для которой ищем корень
    x0 - начальное приближение
    tol - допустимая погрешность
    max_iter - максимальное количество итераций
    
    Возвращает:
    x - найденный корень
    iterations - количество итераций
    """
    x = x0
    iterations = 0
    
    h = 1e-6
    J = (f(x + h) - f(x)) / h
    
    while iterations < max_iter:
        fx = f(x)
        if abs(fx) < tol:
            return x, iterations
            
        dx = -fx / J
        x_new = x + dx
        fx_new = f(x_new)
        
        J = J + (fx_new - fx - J * dx) / dx
        
        x = x_new
        iterations += 1
        
    raise Exception("Метод не сошелся за максимальное число итераций")


def f(x):
    return x**3 + x**2 - 4

x0 = 2.0

root, iters = newton_broyden(f, x0)
print(f"Найденный корень: {root}")
print(f"Количество итераций: {iters}")
print(f"Значение функции в корне: {f(root)}")
