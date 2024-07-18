n = int(input("Nhap n: "))
t = 0
for val in range(1, 2 * n + 2):
    if val % 2 == 0:
        t = t - val
    else:
        t = t + val
print(t)