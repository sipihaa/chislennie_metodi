import numpy as np
from scipy.special import factorial


def iterative_method(A, t, iterations=400):
    res = np.eye(2)

    for k in range(1, iterations):
        res += ((A * t)**k) / factorial(k)

    return res


A = np.ones((2, 2)) / 2
t_list = [1, 5, 10]
for t in t_list:
    print(f'При t = {t}, выражение exp(At) равно:')
    print(iterative_method(A, t))
