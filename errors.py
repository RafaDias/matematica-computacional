from functions import ff, fff, ffff


def error_global(expected, result):
    return ((expected - result) / expected) * 100


def error_local(x, y, h):
    errorLocal = ff(x-h)/2 * h ** 2 + (fff(x - h)/6) * h ** 3 + (ffff(x - h)/24)* h ** 4
    return errorLocal * 100 / y