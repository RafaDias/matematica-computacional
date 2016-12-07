from functions import f, f_exact
from utils import print_header, print_t
from errors import error_global, error_local


def heun(x, y, h, n):
    print_header(x, y)
    for i in range(n):
        y1 = y + f(x,y) * h;
        a = (f(x,y) + f(x+h, y1)) / 2
        y = y + a * h;
        x = x + h;
        print_t(x, f_exact(x), y, error_global(f_exact(x), y), error_local(x, f_exact(x), h))

if __name__=='__main__':
    heun(0, 1, 0.5, 4)