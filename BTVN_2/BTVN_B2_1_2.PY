n = int(input("Nhap so nguyen duong n: "))
t  = 0
for val in range(1, n+1):
    # print(val)
    if n % val == 0:
        t = t + val
print(t)