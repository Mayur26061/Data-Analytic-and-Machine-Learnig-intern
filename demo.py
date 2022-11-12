def kangaroo(x1, v1, x2, v2):
    i = 0
    while (x1 < x2):
        x1 = x1 + v1
        x2 = x2 + v1
        if x1 == x2:
            print("yes")
            break

    print("no")


kangaroo(0, 2, 5, 3)