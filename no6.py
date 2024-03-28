for i in range (5, 0, -1):
    for j in range (1, i + 1):
        if j < i:
            print("+", end=" ")
        else:
            for k in range (j, 6):
                print(k, end=" ")
    print()
