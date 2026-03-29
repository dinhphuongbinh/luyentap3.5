#bai1
a = int(input("Nhập số a: "))   
if a % 2 == 0:  
    print("a là số chẵn")
else:
    print("a là số lẻ ")
#bai2
a = int(input("do dai canh a: "))
b = int(input("do dai canhb: "))
c = int(input("do dai canh c: "))   
if a>0 and b>0 and c>0:  
    print("do dai 3 canh la: ",a,b,c)   
else:
    print("it nhat một canh co độ dai khong hop le")
#bai3
import time
nam_sinh = int(input("Nhap nam sinh: "))
nam_hien_tai = time.localtime().tm_year
tuoi = nam_hien_tai - nam_sinh
print(f"Nam sinh {nam_sinh}, vay ban {tuoi} tuoi.")
