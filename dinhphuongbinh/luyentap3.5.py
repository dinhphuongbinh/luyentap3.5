#bai4
n = int(input("Nhap so nguyen duong: "))
if n % 2 == 0 and n % 3 == 0:
    print("So chia het cho ca 2 va 3")
elif n % 2 == 0:
    print("So chia het cho 2")
elif n % 3 == 0:
    print("So chia het cho 3")
else:
    print("So khong chia het cho 2 va 3")

#bai5
import math
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))
if a == 0:
    print("day khong phai phuong trinh bac 2")
else:
    delta = b**2 - 4*a*c
    
    if delta < 0:
        print("Phuong trinh vo nghiem")
    elif delta == 0:
        x = -b / (2*a)
        print("Phuong trinh co nghiem kep x =", x)
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print("Phuong trinh co 2 nghiem:")
        print("x1 =", x1)
        print("x2 =", x2)