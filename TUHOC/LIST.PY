#list tương tự như cấu trúc dữ liệu mảng trong các ngôn ngữ lập trình khác nhưng linh hoạt hơn nhiều 
#lists are ordered: các phần tử trong list là có thứ tự 
#Accessed by index: truy cập các phần tử trong list thông qua chỉ số 
#lists can contain any sort of object: list có thể chứa các object thuộc dữ liệu khác nhau như int, str, float, và có thể là một list khác 
# #lists are changeable(mutable): các phần tử trong list có thể thay đổi giá trị, các thao tác thêm, xóa các phần tử cũng đc hổ trợ
# s = "28teach"
# a = list(s)#hàm list() biến đổi các object thành list
# print(a)
# #hàm len() để biết số lượng phần tử trong list
# a = [1, 2, 3, 4, "python"]
# print(len(a))
# #có thể truy cập đến các giá trị trong list thông qua chỉ số giống mảng 
# a=[1, 2, 3, 4, "python"]
# print(a[0])
# print(a[2])
# print(a[-3])
# #duyệt list thông qua chỉ số 
# a = [1, 2, 3, 4, 5, "python"]

# for i in range(len(a)):
#     print(a[i], end=' ')
# print()
# for i in range(-1, len(a) * -1 -1, -1):
#     print(a[i], end=' ')
# print()
# #duyệt bằng for each
# a = [1, 2, 3, 4, 5, "python"]

# for i in a: 
#     print (i, end=' ')
#thay đổi giá trị phần tử 
# a= [1, 2, 3, 4, 5, "python"]

# a[-1] = "duong"
# a[-2] = "hoàng"
# print(a)
#thêm một phần tử vào list sủ dụng hàm append()
a = [1, "python", 'dương']

a.append("c#")
a.append("java")
print(a)
#thêm một phần tử vào list ở một vị trí bất kì 
a=["apple", 1, 2, 3,"python", ]

a.insert(1, "facebook")
a.insert(3, "hoàng")
print(a)