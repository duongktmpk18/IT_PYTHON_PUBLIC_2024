n = int(input("Nhap vao mot so nguyen duong N: "))
t = 0
while n > 0:
     t = t + (n % 10)
     n = n // 10
print(t)