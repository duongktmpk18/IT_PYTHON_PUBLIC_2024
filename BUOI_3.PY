# toán tử trong string 
# =, +, *, [], in, not in,..
# ghép hai xâu "+"
# nhân xau "*"
#duyệt xâu
# s1 = "python 123"
# # for i in s1:
# #     print(i, end=' ')
# # print()
# # for i in range(len(s1)):
#     # print(s1[i], end=' ')
# # string có hai index 
# # số dương bắt đầu từ 0 còn số âm bắt đầu từ -1 và lùi dần
# for i in range(len(s1)):
#     print(s1[i], end=' ')
# print(s1[-1: -3: 2])
#chuỗi là bất biến không thể chèn hay xóa một hay nhiều kí tự chỉ có thế thayu thế hoặc xóa chuổi 
# del s1 xóa một chuỗi
#một sô phương thức xử lý chuỗi
# lower() trả về một chuỗi viết thường 
# upper() trả về một chuổi viết hoa
# split() phân tách chuỗi thành list
# strip() trả về chuỗi đã đc tối giản hóa 
# join() nốt các chuỗi lại với nhau tương tụ như "+"
# len() trả về độ dài của chuỗi
# find() tìm kiếm xâu con
# # replace () thay thế cụm ký tự 
# a = "Hoàng Minh Dương"
# b = "KTMP_03"
# print(a.lower())
# print(a.upper())
# print(a.split())
# print(a.strip())
# print(a.join("123"))#str.join("str") nối cái a vào giữa các ký tự trong join ()
# print(a.find("n"))
# print(a.replace("n", "1", 2))# str.replace(old, new, count)
# ví dụ
# s = input("Nhap chuỗi: ")
# s = s.split()
# print(len(s))
# print(len(input().split()))
# một số phương thức xác thực chuỗi
# đọc thêm
#list danh sách:
# list lồng nhau bằng dấu ","
# l = [1, [2,3,[4,5]], 7]
# print(l)
# #list comprehension
# l = [x for x in range(10)]
# print(l)
# a = [int(input()) for _ in range(10)]
# print(a)
#list comprehension lồng nhau
# v = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# # l = []
# # for i in v:
# #     for y in i:
# #         l.append(y)
# # print(y)
# l = [num for i in v for num in i]
# print (l)
#list comprehension vs if 
# l =[i for i in range(10) if i % 2 == 0]
# print(l)
#truy xuat list
# l = [1, 2, 3, 4]
# l1 = l[1; 3] #using slicing 
# l2 = l[:: 2] #step bang 2
#ung dung cua slicing
# l = [1, 2, 3, 4]
# l1 = l[::-1]

# l =[1, 2, 3, 4]
# # # sua 
# l[1:] = [10, 9, 8]
# print (l)
# #chen
# l[:-3] = [10, 9, 8]
# print(l)
# # xoa
# # l[:] = []
# # print(l)
# n = int(input())
# a = [int(input()) for _ in range(n)]
# b = [int(input()) for _ in range(n)]
# # print

# a.sort()
# print(a)

# #b
# b1 = b.copy()
# print (b1)
# b.reverse()
# print (b)
# b.extend(a)
# # print (b)
# b = b* 2
# b = b[::-1]
# c = b + a
# a = list(map(int, input().split())) cach nhap khac 
n = int(input())
cnt = 0
for i in range(1, n +1):
    d = 0
    for j in range(1, n +1):
        if i % j == 0:
            d += 1
    if d == 2:
        cnt += 1
print(cnt)