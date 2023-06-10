'''
a = 123
b = "hahaha"
print("a=",a)
print("b=",b)
print("a+b=", str(a) +" "+ b )
'''
#comment# Bài thực hành 1
'''
Ten = input("Ten:")
Ho = input("Ho:")
Tuoi = input ("Tuoi:")
print("Họ và tên:", Ho, Ten)
print("Hiện tại:", Tuoi, "Tuổi")
'''
#comment# Bài thực hành 2
'''
comp = "Người phỏng vấn:"
print(comp, "Bạn là nam hay nữ")
Sex = input ("Nam or Nữ:")
print(comp, "Bạn thích ăn gì")
Food = input ("Món ăn yêu thích:")
print(comp, "Thú cưng bạn bị dị ứng với gì")
Pet = input ("Thú cưng bạn bị dị ứng với gì:")
print(comp , "Đây là tất cả câu trả lời của bạn")
print("Nam or Nữ:", Sex)
print("Bạn thích ăn gì:", Food)    
print("Thú cưng bạn bị dị ứng với gì:", Pet)
'''

#comment# Thực hành 3
'''
a =  float(input("a = "))
b =  float(input("b = "))
c =  float(input("c = "))

print("(a+b+c)/3 =", (a + b + c) / 3)
'''
#comment# Thực hành 4
VND = 35205000
DOLA = 1500
print("1 đô la =", float(VND / DOLA), "VND")
luong = 1257125
e = int(VND / luong) + 1
print("Sau", e, "tháng")
print("Ta sẽ có:",e * luong, "VND")
print("Ta sẽ có:" ,luong * (e / float(VND/DOLA)), "DOLA")