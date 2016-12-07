def print_t(x, y, exact_x, error_global, error_local):
    print("{:.4f}    \t {:.4f}    \t {:.4f}    \t {:.4f} %      {:.4f}".format(
        x, y, exact_x, error_global, error_local)
    )


def print_header(x, y):
    print("{:^8}\t {:^8}\t {:^8}\t {:^8}\t {:^8}\n\n".format("X", 
        "Y Verdadeiro", "Y", "Erro global", "Erro Local"))   
    print("{:^8}\t {:^8}\t {:^8}\t --".format(x, y, y))