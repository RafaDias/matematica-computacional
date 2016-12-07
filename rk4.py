# coding: utf-8

def f(x, y):
    #return -2 * x**3 + 12 * x **2 - 20 * x + 8.5
    return y * x ** 2 - 1.1 * y #Exercício 25.5


def f_exact(x, y):
    return 2 * x * y


def rk4(x, y, h, n):
    print("X\t Y\t Erro máximo\n")
    print("{}\t {}\t --".format(x, y))
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
        print("{:.4f}\t {:.4f}\t {:.4f}%".format(x, y, y*100))

if __name__=='__main__':
    rk4(0, 1, 0.5, 4)