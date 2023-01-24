class Rational:
    def __init__(self, nominator, denominator):
        self.nominator = nominator
        self.denominator = denominator

    def clone(self):
        return Rational(self.nominator, self.denominator)

    def add(self, number):
        if number.denominator == self.denominator:
            self.nominator += number.nominator
        else:
            self.nominator = self.nominator*number.denominator + number.nominator*self.denominator
            self.denominator = self.denominator*number.denominator
        self.shorten()

    def sub(self, number):
        if number.denominator == self.denominator:
            self.nominator -= number.nominator
        else:
            self.nominator = self.nominator*number.denominator - number.nominator*self.denominator
            self.denominator = self.denominator*number.denominator
        self.shorten()

    def mul(self, number):
        self.nominator = self.nominator*number.nominator
        self.denominator = self.denominator*number.denominator
        self.shorten()

    def div(self, number):
        self.nominator = self.nominator*number.denominator
        self.denominator = self.denominator*number.nominator
        self.shorten()

    def shorten(self):
        if self.nominator is not 0:
            nominator_parts = []
            nominator_placeholder = self.nominator
            for x in range(2, self.nominator+1):
                while nominator_placeholder % x == 0:
                    nominator_parts.append(x)
                    nominator_placeholder = nominator_placeholder / x
            denominator_parts = []
            denominator_placeholder = self.denominator
            for x in range(2, self.denominator+1):
                while denominator_placeholder % x == 0:
                    denominator_parts.append(x)
                    denominator_placeholder = denominator_placeholder / x
            for part in nominator_parts:
                if part in denominator_parts:
                    denominator_parts.remove(part)
                    self.nominator = self.nominator/part
                    self.denominator = self.denominator/part


def test_adding():
    liczba1 = Rational(1, 2)
    liczba2 = Rational(1, 2)
    liczba1.add(liczba2)

    assert liczba1.nominator == 1


def test_substracting():
    liczba1 = Rational(1, 2)
    liczba2 = Rational(1, 2)
    liczba1.sub(liczba2)

    assert liczba1.nominator == 0


def test_multiplying():
    liczba1 = Rational(1, 2)
    liczba2 = Rational(1, 2)
    liczba1.mul(liczba2)

    assert liczba1.denominator == 4


def test_dividing():
    liczba1 = Rational(1, 2)
    liczba2 = Rational(1, 2)
    liczba1.div(liczba2)

    assert liczba1.nominator == 1


def test_shortening():
    liczba1 = Rational(48, 96)
    liczba1.shorten()

    assert liczba1.nominator == 1
