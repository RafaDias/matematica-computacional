def f(x, y):
    return -2 * x**3 + 12 * x **2 - 20 * x + 8.5

def rk4(x, y, h, n):
    for i in range(n):
        f1 = f(x,y)
        x0 = x + h / 2
        y0 = y + f1*h/2
        f2 = f(x0,y0)
        y0 = y + f2*h/2
        f3 = f(x0,y0)
        x0 = x + h
        y0 = y + f3*h
        f4 = f(x0,y0)
        y = y + (f1 + 2*f2 + 2*f3 + f4)*h/6
        x = x + h
        print(x, y)

rk4(0, 1, 0.5, 8)