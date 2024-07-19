#s = str('duong')
#print (s)
#a= [1, 2, 3]
#print (type(s))
#print (a[]) 
#t = (1)
#print(type(t))
#my_dict = {
#    "Ten": "An",
#    "Gioi tinh": "Nam",
#    "Nam sinh": 2005
#}
#print(type(my_dict))
#d = dict() #or d = dict{}
#print(type(d))
#print (ojbects, set= '', end='\n', file=sys.stdout, flush=false)
#for i in range(5):
 #   print (t, and= ' ')
# a  = 5 
# b = 9
# print ('{} {}'.format(a, b))
# print (f'{a} + {b} ={a + b}')
# c = str('hoang')
# d= str('minh')
# e = str('duong')
# # print ('{} {} {}'.format(c, d, e))
# print(f'{c} {d } {e}')
# print (a - b )
# print ('{} ** {}'.format(a, b,))
# print (f'{a} * {b} = {a * b}')
# print (a // b)
# print (a%b)
# print (a/ b)
# print (a ** b)
# x = 1
# print (x < 2 and x < 12)
# print (x < 3 or x > 10)
# print (not(x < 6 and x < 10))
#in tra ve true neu bien do o trong mot chuoi, list,... chi dinh
#not in nguoc lai voi in 
# cac toan tu khac la: +=, -=, *=, /=, %=, **=, //=.
# toan tu nhan dang: is (tra ve true neu 2 bien cung tro den mot o nho) is not (nguoc lai)
# print (a is b)
# print (a is not b)
#bitwise operators 
#& (AND)  
#| (OR)
#^ (XOR)
#~ (NOT)
# >> (left shift)
# << (right shift)
# print (a & b)
# print (a | b)
# print (a ^ b)
# print (~a)
# print (a << a)
# print (b >> b)
#if else trong python
#   if <expr>:
#       <statement>
# if a < b:
#     print ('a nho hon b')  
# else: 
#     print ('a lon hon b') 
# #if ... elif .. else 
# a = int(input())
# b = int(input())
# c = int(input())
# if a < b: 
#     print ('a nho hon b')
# elif a < c and a < b :
#     print('a nho hon c va nho hon b')
# elif a > b and a > c:
#     print ('a lon hon b va a lon hon b')
# elif a is b and a is c:
#     print ('a bang ca b va c')
# else: 
#     print ('truong hop khac')

# d = int(input())
# e = int(input())
# # result = d + e if d < e else d - e
# print (result)
#gia tri falsy bao gom: {}, [], (), set(), "", range(0),0, 0.0, 0j, none, false.
#gia tri truthy bao gom: cac trinh tu khong rong (list, tuples, strings, dict, sets,...
#    cac gia tri so khac 0
#    cac hang so la true
#   Note co the check falsy va truthy bang bool()
# Vong lap 
# for <var> in <interable>
    # <statement(s)>
# my_list  = ["1", "1", "1"]
# for so in my_list:
#     print (so)
# for val in range(0, 10): # ham range(bat dau, ket thuc, buoc nhay(neu can thay doi mac dinh bang 1))
#     print (val)
# my_list = ["d", "u", "o", "n", "g"]
# for danh_van in my_list:
#     print (danh_van, end=' ')
#while <cau lenh>:
#   code
#break, continue giong trong C++
#lenh pass khi vaong lap khong co gi de khong bi loi 
# i = (2, 4, 6)
# print (i[1]) #Note
# print (i[-2])
# a = 10
# while a > 5:
#     print (a, end=' ')
#     a -=  1
# ham enumerate(interable,  start index new)
a = [1, 2, 3, 5, 7]
# for index, val in enumerate(a, 2):
#     print (index, val)
#ket hop while va for voi else 
#khi vong lap ket thuc else  moi dc chay 
#neu co lech break truoc thi bo qua else 
for val in a:
    print(val)
    # break
else:
    print ("truong hop khac")
