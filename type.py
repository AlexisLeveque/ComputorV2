from math_func import ft_pow

class Rationels:
    def __init__(self, nbr):
        self.nbr = nbr
        self.is_positif = True if nbr >= 0 else False

    def add(self, nbr):
        if type(nbr, Rationels):
            return self.nbr + nbr
        if type(nbr, Complex):
            return Complex(self.nbr + nbr.r, nbr.i)

    def sous(self, nbr):
        if type(nbr, Rationels):
            return self.nbr - nbr
        if type(nbr, Complex):
            return Complex(self.nbr - nbr.r, nbr.i)

    def mult(self, nbr):
        if type(nbr, Rationels):
            return self.nbr * nbr
        if type(nbr, Complex):
            return Complex(self.nbr - nbr.r, nbr.i)

    def div(self, nbr):
        if type(nbr, Rationels):
            return self.nbr / nbr
        if type(nbr, Complex):
            return Complex(self.nbr - nbr.r, nbr.i)

    def mod(self, nbr):
        return "Error"

    def pow(self, nbr):
        if type(nbr, Rationels):
            return ft_pow(self.nbr, nbr)
        if type(nbr, Complex):
            return Complex(self.nbr - nbr.r, nbr.i)


class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
