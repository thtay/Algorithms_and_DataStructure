import math


class Fraction:
    def __init__(self, top, bottom):

        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, otherfraction):
        newnum = self.num * otherfraction.den + self.den * otherfraction.num
        newden = self.den * otherfraction.den
        common = math.gcd(newnum, newden)

        return Fraction(newnum // common, newden // common)


myf = Fraction(3, 5)
print(myf)