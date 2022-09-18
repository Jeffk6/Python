q = int(input("Enter num: "))
e = int(input("Enter num: "))
w = int(input("Enter num: "))
t = int(input("Enter num: "))
u = int(input("Enter num: "))
i = int(input("Enter num: "))
o = int(input("Enter num: "))
p = int(input("Enter num: "))

if q == 1:
  num1 = 1
else:
  num1 = 0

if e == 1:
  num2 = 2
else:
  num2 = 0

if w == 1:
  num4 = 4
else:
  num4 = 0

if t == 1:
  num8 = 8
else:
  num8 = 0

if u == 1:
  num16 = 16
else:
  num16 = 0

if i == 1:
  num32 = 32
else:
  num32 = 0

if p == 1:
  num64 = 64
else:
  num64 = 0

if o == 1:
  num128 = 128
else:
  num128 = 0

x = num1 + num2 + num4 + num8 + num16 + num32 + num64 + num128


print("=", x)

while True:
  i=0
  i+1