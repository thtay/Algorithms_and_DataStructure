"""
What Does It Take to Be An Expert At Python
Notebook based off James Powell's talk at PyData 2017'
https://www.youtube.com/watch?v=7lmCu8wz8ro
If you want to become an expert in Python, you should definitely
watch this PyData talk from James Powell.

Video Index
metaclasses: 18:50
metaclasses(explained): 40:40
decorator: 45:20
generator: 1:04:30
context manager: 1:22:37
summary: 1:40:00
"""


class Polynomial:
    def __init__(self, *coeffs):
        self.coeffs = coeffs

    def __repr__(self):
        return "Polynomial(*{!r})".format(self.coeffs)

    def __len__(self):
        return len(self.coeffs)

    def __call__(self):
        pass

    def __add__(self, other):
        return Polynomial(*(x + y for x, y in zip(self.coeffs, other.coeffs)))


# p = Polynomial(1, 2, 3)
# print(p)
# print(len(p))

# p1 = Polynomial(1, 2, 3)
# p2 = Polynomial(3, 4, 3)
# print(p1 + p2)


class Base:
    def food(self):
        return "foo"


assert hasattr(Base, "foo")
