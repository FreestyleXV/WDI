a = int(input("podaj: "))

for x in range(0, a):
    print(" "*(a-x)+"*"*(x*2+1))
print(" "*a+"U")