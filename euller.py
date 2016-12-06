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


def error_global(expected, result):
    return ((expected - result) / expected) * 100


def error_local(x, y, h):
    errorLocal = ff(x-h)/2 * h ** 2 + (fff(x - h)/6) * h ** 3 + (ffff(x - h)/24)* h ** 4
    return errorLocal * 100 / y


def print_t(x, y, exact_x, error_global, error_local):
    print("{:.4f}    \t {:.4f}    \t {:.4f}    \t {:.4f} %      {:.4f}".format(
        x, y, exact_x, error_global, error_local)
    )


def print_header(x, y):
    print("{:^8}\t {:^8}\t {:^8}\t {:^8}\t {:^8}\n\n".format("X", 
        "Y Verdadeiro", "Y Euller", "Erro global", "Erro Local"))   
    print("{:^8}\t {:^8}\t {:^8}\t --".format(x, y, y))


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