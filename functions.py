def f(x, y):
    return -2 * x**3 + 12 * x **2 - 20 * x + 8.5


def ff(x):
    return - 6 * x ** 2 + 24 * x - 20


def fff(x):
    return - 12 * x + 24


def ffff(x):
    return - 12


def f_exact(x):
    return - 0.5 * x ** 4 + 4 * x ** 3 - 10 * x ** 2 + 8.5 * x + 1