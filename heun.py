from math import e


def f(x, y):
    return 4 * e ** (0.8 * x) - 0.5 * y


def heun(x, y, h, n):
    print(x, y)
    for i in range(n):
        y1 = y + f(x,y) * h;
        a = (f(x,y) + f(x+h, y1)) / 2
        y = y + a * h;
        x = x + h;
        print(x, y)

heun(0, 2, 1, 4)