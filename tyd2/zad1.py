M = input("Podaj liczbę z zakresu od 1 do 10000: ")

M = int(M)

if M < 1:
    print("Liczba za mała")
elif M > 10000:
    print("Liczba za duża")
else:
    tab = [1]
    tab2 = [0]
    lastFactorial = 1
    if M > 1:
        for x in range(2, M+1):
            lastFactorial = lastFactorial*x
            tab.append(lastFactorial)
            tab2.append(lastFactorial-tab[x-2])
    print(tab)
    print(tab2)
