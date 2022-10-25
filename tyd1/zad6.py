# Tu liczby biore
a = int(input("Podaj liczbę"))
b = int(input("Podaj liczbę"))

"""
    To jest wieloliniowy komentarz
"""

# A tu sobie je sprawdzam
if a < 0 and b < 0:
    print("nie wyszło")
else:
    if a < 0:
        a = -a
    elif b < 0:
        b = -b
    # Obliczęnia
    c = a + b
    d = a - b
    e = a * b
    f = a / b
    g = a ** 2
    h = b ** 2
    i = a ** 0.5
    j = b ** 0.5
    print("suma " + str(c))
    print("różnica " + str(d))
    print("iloczyn " + str(e))
    if e == 10:
        print("Yay!")
    print("iloraz " + str(f))
    print("pierwsza liczba do 2 " + str(g))
    print("druga liczba do 2 " + str(h))
    print("pierwsza liczba pierwiastek " + str(i))
    print("druga liczba pierwiastek " + str(j))
