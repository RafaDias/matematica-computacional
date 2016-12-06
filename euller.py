def f(x, y):
    return -2 * x**3 + 12 * x **2 - 20 * x + 8.5


def f_exact(x):
    return - 0.5 * x ** 4 + 4 * x ** 3 - 10 * x ** 2 + 8.5 * x + 1


def error_global(expected, result):
    return ((expected - result) / expected) * 100


def print_as_t(x, y, exact_x, error_global):
    print("{:.4f}    \t {:.4f}    \t {:.4f}    \t {:.4f} %    \t".format(
        x, y, exact_x, error_global)
    )


def euler(a, b, h, xi, yi):
    x = xi
    y = yi
    print("{:^8}\t {:^8}\t {:^8}\t {:^8}\n\n".format("X", "Y Verdadeiro", "Y Euller", "Erro global"))   
    print("{:^8}\t {:^8}\t {:^8}\t --".format(x, y, y))
    while a < b:
        y += h * f(x, y)
        x += h
        print_as_t(x, y, f_exact(x), error_global(f_exact(x), y))
        a += h


if __name__=='__main__':
    euler(0, 4, 0.5, 0, 1)