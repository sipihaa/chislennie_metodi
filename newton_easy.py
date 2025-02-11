from copy import copy


def derivative(func):
    derivative_func = copy(func)
    for stepen in range(len(func)):
        derivative_func[stepen] = stepen * func[stepen]

    return derivative_func


def f(func, x):
    value = 0
    for stepen in range(len(func)):
        value += func[stepen] * (x ** stepen)

    return value


def newton_method(func, x0=1.0, E=1e-6):
    x_n = x0
    func_derivative = derivative(func)
    f_x_derivative = f(func_derivative, x_n)

    while True:
        f_x = f(func, x_n)
        x_n1 = x_n - f_x / f_x_derivative

        if abs((x_n1 - x_n) / (1 - (x_n1 - x_n) / (x_n - x_n1))) < E:
            return x_n1

        x_n = x_n1


func = [-5, 2, 1]
print(newton_method(func, 2.0))
