a = 0
b = 1
print(a)
print(b)
while (a+b) < 1000000:
    c = a + b
    a = b
    b = c
    print(c)