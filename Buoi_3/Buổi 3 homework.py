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
'''
VND = 35205000
DOLA = 1500
print("1 đô la =", float(VND / DOLA), "VND")
luong = 1257125
e = int(VND / luong) + 1
print("Sau", e, "tháng")
print("Ta sẽ có:",e * luong, "VND")
print("Ta sẽ có:" ,luong * (e / float(VND/DOLA)), "DOLA")
'''
#comment# Bài tập về nhà 
    
#Bài 1
'''
while True :
    while True:
        VND = input("Vui lòng nhập số tiền bạn muốn quy đổi ( VND ):")
        int(VND)
        print("Bạn muốn quy đổi", VND , "VND ?")
        print("Vui lòng nhập Yes / No")
        access = input("Yes / No:")
        if access == "Yes":
            print("Vui lòng chọn mệnh giá bạn muốn quy đổi:")
            print("USD / EUR / JPY / GBP / CHF / AUD / CAD ")
            chose = input("Mệnh giá muốn quy đổi:")
            #USD
            if chose == "USD":
                print("Với",VND, "VND", ", bạn sẽ quy đổi sang được:", int(VND) / 23700, "USD")
                print("Cảm ơn bạn đã sử dụng dịch vụ của chúng tôi")
                break
            
            #EUR
            if chose == "EUR":
                print("Với",VND, "VND", ", bạn sẽ quy đổi sang được:", int(VND) / 25354 , "EUR")
                print("Cảm ơn bạn đã sử dụng dịch vụ của chúng tôi")
                break

            #JPY
            if chose == "JPY":
                print("Với",VND, "VND", ", bạn sẽ quy đổi sang được:", int(VND) / 170 , "JPY")
                print("Cảm ơn bạn đã sử dụng dịch vụ của chúng tôi")
                break
                
            #GBP
            if chose == "GBP":
                print("Với",VND, "VND", ", bạn sẽ quy đổi sang được:", int(VND) / 29471 , "GBP")
                print("Cảm ơn bạn đã sử dụng dịch vụ của chúng tôi")
                break
                
            #CHF
            if chose == "CHF":
                print("Với",VND, "VND", ", bạn sẽ quy đổi sang được:", int(VND) / 26156, "CHF")
                print("Cảm ơn bạn đã sử dụng dịch vụ của chúng tôi")
                break
                
            #AUD
            if chose == "AUD":
                print("Với",VND, "VND", ", bạn sẽ quy đổi sang được:", int(VND) / 15838, "AUD")
                print("Cảm ơn bạn đã sử dụng dịch vụ của chúng tôi")
                break
                
            #CAD
            if chose == "CAD":
                print("Với",VND, "VND", ", bạn sẽ quy đổi sang được:", int(VND) / 17692, "CAD")
                print("Cảm ơn bạn đã sử dụng dịch vụ của chúng tôi")
                break
                
            else:
                print("Vui lòng nhập đúng cú pháp")
                break
            
        if access == "No" :
            break
        else:
            print("Vui lòng nhập đúng cú pháp")
            break
'''

#Bài 2
'''
r = input("Bán kính của hình tròn (cm):")
pi = 3.14
print("Chu vi của hình tròn:", 2*float(r)*float(pi),"cm")
print("Diện tích của hình tròn:", float(r)**float(r)*pi, "cm2")
'''

#Bài 3
A = input("Thời gian về đích của vận động viên A (giây):")
B = input("Thời gian về đích của vận động viên B (giây):")
C = input("Thời gian về đích của vận động viên C (giây):")
Dtb = (float(A) + float(B) + float(C))/3
print("Thời gian về đích của vận động viên A:", A,"giây")
print("Thời gian về đích của vận động viên B:", B,"giây")
print("Thời gian về đích của vận động viên C:", C,"giây")
print("Dtb =", Dtb, "giây")