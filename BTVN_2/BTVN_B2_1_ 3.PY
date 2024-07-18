a = int(input("Nhap so nguyen duong a: "))
b = int(input("Nhap so nguyen duong b: "))
c = int(input("Nhap so nguyen duong c: "))

if a + b > c and a + c > b and c + b > a:
    if a == b and a == c and c == b:
        print("Tam giac deu")
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("Tam giac vuong")
    elif a == b or a == c or b == c:
        print("Tam giac can")
    elif a + b > c  and a + c > b and b + c > a:
        print("Tam giac tu")
    else :
        print("Tam giac nhon")
else:
    print("ba canh khong tao thanh tam giac")