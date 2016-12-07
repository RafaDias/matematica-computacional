def middle_point(x, y, h, n):
    print(x, y)
    for i in range(n):
        y1 = y + f(x,y) * h / 2;
        x1 = x + h / 2
        y = y + f(x1, y1) * h
        x = x + h;
        print(x, y)

middle_point(0, 1, 0.5, 8)