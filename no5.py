b=2
for i in range (1, 6):
    a = i
    for j in range (5):
        print(a, end=" ")
        a += b
    b += 1
    print()