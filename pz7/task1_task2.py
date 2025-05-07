import numpy as np


def rotation_method(A, eps=1e-500, max_iter=10000000):
    n = len(A)
    
    V = np.eye(n)
    
    D = A.copy()
    
    for iteration in range(max_iter):
        max_val = 0
        p, q = 0, 0
        
        for i in range(n):
            for j in range(i + 1, n):
                if abs(D[i, j]) > max_val:
                    max_val = abs(D[i, j])
                    p, q = i, j
        
        if max_val < eps:
            return np.diag(D), V, iteration
        
        tan_2alpha = 2 * D[p, q] / (D[p, p] - D[q, q])
        alpha = np.arctan(tan_2alpha) / 2
        
        H = np.eye(n)
        c = np.cos(alpha)
        s = np.sin(alpha)
        H[p, p] = c
        H[q, q] = c
        H[p, q] = -s
        H[q, p] = s
        
        D = H.T @ D @ H
        
        V = V @ H

        print(iteration)
    
    raise Exception("Метод не сошелся за максимальное число итераций")


# A = np.array([
#     [2.0, 1.0],
#     [1.0, 3.0]
# ], dtype=float)

A = np.array([
    [5.0, 1.0, 2.0],
    [1.0, 4.0, 1.0],
    [2.0, 1.0, 3.0],
], dtype=float)

values, vectors, iterations = rotation_method(A)

print("Собственные значения:")
print(values)
print("\nСобственные векторы:")
print(vectors)
print(f"\nКоличество итераций: {iterations}")

print("\nПроверка:")
np_values, np_vectors = np.linalg.eig(A)
print("\nСобственные значения numpy:")
print(np_values)
print("\nСобственные векторы numpy:")
print(np_vectors)
