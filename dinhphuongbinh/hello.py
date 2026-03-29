a = 16
b = 3
c = 5

print("phep toan so hoc")
print(a + b + c)
print(a - b - c)
print(a * b * c)
print(a / b / c)
print(a ** b ** c)

print("\n phep so sanh ")
print(a > b and b > c)
print(a < b or b < c)
print(a == b)
print(a != c)

print("\n phep gan")

x = a
x += b + c
print(x)

x = a
x -= b + c
print(x)

x = a
x *= b * c
print(x)

x = a
x /= b * c
print(x)

print("\n phep logic ")
print((a > b) and (b < c) and (a > c))
print((a < b) or (b < c) or (a < c))
print(not (a > b and b > c))

print("\nbit")
print(a & b & c)
print(a | b | c)
print(a ^ b ^ c)
print(~a)
print(a << 3)
print(a >> 2)