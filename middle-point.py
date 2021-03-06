from functions import f, f_exact
from utils import print_header, print_t
from errors import error_global, error_local


def middle_point(x, y, h, n):
    print_header(x, y)
    for i in range(n):
        y1 = y + f(x,y) * h / 2;
        x1 = x + h / 2
        y = y + f(x1, y1) * h
        x = x + h;
        print_t(x, f_exact(x), y, error_global(f_exact(x), y), error_local(x, f_exact(x), h))

if __name__=='__main__':
    middle_point(0, 1, 0.5, 4)