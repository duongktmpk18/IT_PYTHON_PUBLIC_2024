n = int(input("Nhap n: "))

for a in range(1, n + 1):
    for b in range(1, n + 1 - a):
        print(" ", end=' ')
    for b in range(1, 2*a):
        print("*", end=' ')
    print()