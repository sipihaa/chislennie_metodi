import numpy as np
from scipy.special import factorial


def iterative_method(A, theta=np.pi / 4, iterations=100):
    res = np.eye(2, dtype=complex)
    i = 1j
    t = i * theta

    for k in range(1, iterations):
        res += ((A * t)**k) / factorial(k)

    return res


A = np.ones((2, 2)) / 2
theta = np.pi / 4

print(f'При θ = {theta:.3f}, выражение exp(A * i * θ) равно:')
result = iterative_method(A, theta)
formatted_result = np.array([[f"{x.real:.3f}{x.imag:+.3f}i" for x in row] for row in result])
print(formatted_result)
