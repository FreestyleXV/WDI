a = int(input("podaj początek: "))
b = int(input("podaj koniec: "))

if b - a > 20:
    liczby = list(range(a, b+1))
    print(liczby)
    c = 0
    d = 0
    while c < len(liczby):
        d += liczby[c]
        c += 1
    e = d/len(liczby)
    for i, x in enumerate(liczby):
        if x > e:
            if liczby[i-1] == e:
                print(liczby[i-4])
                print(liczby[i-3])
                print(liczby[i-2])
            else:
                print(liczby[i-3])
                print(liczby[i-2])
                print(liczby[i-1])
            print(liczby[i])
            print(liczby[i+1])
            print(liczby[i+2])
            break

else:
    for x in range(a, b+1):
        print(x)
