from functions import f, f_exact
from utils import print_header, print_t
from errors import error_global, error_local


def euler(a, b, h, xi, yi):
    x = xi
    y = yi
    
    print_header(x, y)
    
    while a < b:
        y += h * f(x, y)
        x += h
        print_t(x, f_exact(x), y, error_global(f_exact(x), y), error_local(x, f_exact(x), h))
        a += h


if __name__=='__main__':
    euler(0, 4, 0.5, 0, 1)