import numpy as np


def find_root_intervals(f, a, b, step=0.1):
    """
    Находит интервалы, содержащие корни функции
    
    Параметры:
    f - функция, для которой ищем корни
    a, b - границы области поиска
    step - шаг поиска
    
    Возвращает:
    intervals - список интервалов [a, b], содержащих корни
    """
    intervals = []
    x = a
    
    while x < b:
        if f(x) * f(x + step) <= 0:
            intervals.append([x, x + step])
        x += step
    
    return intervals


def check_root_existence(f, a, b):
    """
    Проверяет существование корня на интервале [a, b]
    используя теорему Больцано-Коши
    
    Параметры:
    f - функция
    a, b - границы интервала
    
    Возвращает:
    bool - существует ли корень на интервале
    """
    return f(a) * f(b) <= 0


def find_all_roots(f, a, b, tol=1e-6, max_iter=100):
    """
    Находит все корни функции на заданном интервале
    
    Параметры:
    f - функция
    a, b - границы области поиска
    tol - допустимая погрешность
    max_iter - максимальное количество итераций
    
    Возвращает:
    roots - список найденных корней
    """
    intervals = find_root_intervals(f, a, b)
    roots = []
    
    for interval in intervals:
        if check_root_existence(f, interval[0], interval[1]):
            x = interval[0]
            iterations = 0
            
            while iterations < max_iter:
                x_new = x - f(x) * (interval[1] - x) / (f(interval[1]) - f(x))
                
                if abs(x_new - x) < tol:
                    roots.append(x_new)
                    break
                    
                x = x_new
                iterations += 1
    
    return roots


def f(x):
    return x**3 - 2*x**2 - 5*x + 6

a = -10
b = 10

roots = find_all_roots(f, a, b)
print("Найденные корни:")
for i, root in enumerate(roots, 1):
    print(f"Корень {i}: {root}")
    print(f"Значение функции в корне: {f(root)}")
