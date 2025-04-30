import numpy as np


def chord_method(f, a, b, tol=1e-6, max_iter=100):
    """
    Метод хорд для решения нелинейных уравнений
    
    Параметры:
    f - функция, для которой ищем корень
    a, b - границы интервала, содержащего корень
    tol - допустимая погрешность
    max_iter - максимальное количество итераций
    
    Возвращает:
    x - найденный корень
    iterations - количество итераций
    """
    if f(a) * f(b) >= 0:
        raise ValueError("Функция должна иметь разные знаки на концах интервала")
    
    iterations = 0
    x = a
    
    while iterations < max_iter:
        x_new = x - f(x) * (b - x) / (f(b) - f(x))
        
        if abs(x_new - x) < tol:
            return x_new, iterations
            
        x = x_new
        iterations += 1
        
    raise Exception("Метод не сошелся за максимальное число итераций")


def f(x):
    return x**3 + x**2 - 4

a = 1.0
b = 2.0

root, iters = chord_method(f, a, b)
print(f"Найденный корень: {root}")
print(f"Количество итераций: {iters}")
print(f"Значение функции в корне: {f(root)}")
