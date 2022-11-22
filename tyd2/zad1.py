M = input("Podaj liczbę z zakresu od 1 do 10000: ")

# try:
M = int(M)

if M < 1:
    print("Liczba za mała")
elif M > 10000:
    print("Liczba za duża")
else:
    tab = []
    tab2 = [0]
    for x in range(1, M+1):
        if x <= 2:
            tab.append(x)
            if x == 2:
                tab2.append(x-tab[x-2])
        else:
            factorial = 2
            for y in range(3, x+1):
                factorial = factorial*y
            tab.append(factorial)
            tab2.append(factorial-tab[x-2])
    print(tab)
    print(tab2)
# except ValueError:
#     print("Musisz podać liczbę!")