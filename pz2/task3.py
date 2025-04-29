import numpy as np


def simple_iteration_sqrt(a, x0, tol=1e-6, max_iter=100):
    """
    Метод простых итераций
    
    Параметры:
    a - число, из которого извлекаем корень
    x0 - начальное приближение
    tol - допустимая погрешность
    max_iter - максимальное количество итераций
    
    Возвращает:
    x - приближенное значение квадратного корня
    iterations - количество итераций
    """
    x = x0
    iterations = 0
    
    while iterations < max_iter:
        x_new = 0.5 * (x + a / x)
        
        if abs(x_new - x) < tol:
            return x_new, iterations
            
        x = x_new
        iterations += 1
        
    raise Exception("Метод не сошелся за максимальное число итераций")


a = 16.0
x0 = 6.0

sqrt_approx, iters = simple_iteration_sqrt(a, x0)
print(f"Приближенное значение корня из {a}: {sqrt_approx}")
print(f"Точное значение: {np.sqrt(a)}")
print(f"Количество итераций: {iters}")
print(f"Погрешность: {abs(sqrt_approx - np.sqrt(a))}")
