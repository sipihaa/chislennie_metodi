def f(func, x):
    value = 0
    for stepen in range(len(func)):
        value += func[stepen] * (x ** stepen)

    return value


def dichotomy_method(func, x0=-10.0, x1=1.0, E=1e-6):
    if f(func, x0) * f(func, x1) >= 0:
        print('Введите другое начальное приближение')
        return 0

    while True:
        x2 = (x0 + x1) / 2

        if abs(x1 - x0) < E:
            return x1

        if f(func, x0) * f(func, x2) < 0:
            x1 = x2
        elif f(func, x1) * f(func, x2) < 0:
            x0 = x2


func = [-5, 2, 1]
print(dichotomy_method(func))
