n = int(input("Nhap n: "))

for a in range(1, n + 1):
    t = 0
    for b in range(1, a):
        if a % b == 0:
            t = t + b
    if t == a:
        print(a)