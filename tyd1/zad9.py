def checkPin():
    if input("Podaj pin: ") == pin:
        return True
    else:
        if input("Niepoprawny pin. Spróbuj jeszcze raz: ") == pin:
            return True
        else:
            print("Niepoprawny pin. Operacja wstrzymana.")
            return False


command = ""
pin = "1234"
balance = 1000

while command != "koniec":
    command = input("Podaj operację (wpł, wypł, saldo, koniec): ")
    if command == "wpł":
        if checkPin():
            balance += int(input("Podaj kwotę wpłaty (PLN):"))
            print("Gratulacje wpłacono!")
    if command == "wypł":
        if checkPin():
            withdraw = int(input("Podaj kwotę wypłaty:"))
            if withdraw > balance:
                print("Nie masz wystarczających środków.")
            else:
                balance -= withdraw
                print("Wypłacono pomyślnie!")
    if command == "saldo":
        if checkPin():
            print("Twoje saldo (PLN): "+str(balance)+"!")