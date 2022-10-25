from random import randint

do = True

while do:
    a = int(input("Podaj liczbę:"))
    b = int(input("Podaj liczbę:"))
    c = input("Podaj operację:")
    d = 0

    if c == "+":
        d = a + b
    elif c == "-":
        d = a - b
    elif c == "*":
        d = a * b
    elif c == "/":
        d = a / b
    elif c == "#":
        d = a ** (1/b)
    elif c == "^":
        d = a ** b
    elif c == "x":
        if a < b:
            d = randint(a, b)
        else:
            d = randint(b, a)

    print("Wynik Twojej operacji to: "+str(d))
    if input("Czy chcesz wprowadzić nowe dane? ") == "N":
        do = False
