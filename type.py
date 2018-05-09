from __future__ import division
from math_func import ft_pow


class Function:
    def __init__(self, function, var):
        self.func = function
        self.var = var


class Rationels:
    def __init__(self, nbr):
        self.nbr = nbr
        self.is_positif = True if nbr >= 0 else False

    def __str__(self):
        return str(self.nbr)

    def to_str(self):
        return str(self.nbr)

    def add(self, nbr):
        if isinstance(nbr, Rationels):
            res = self.nbr + nbr.nbr
            return Rationels(res)
        if isinstance(nbr, Complex):
            return Complex(self.nbr + nbr.r, nbr.i)

    def sous(self, nbr):
        if isinstance(nbr, Rationels):
            res = self.nbr - nbr.nbr
            return Rationels(res)
        if isinstance(nbr, Complex):
            return Complex(self.nbr - nbr.r, nbr.i)

    def mult(self, nbr):
        if isinstance(nbr, Rationels):
            res = self.nbr * nbr.nbr
            return Rationels(res)
        if isinstance(nbr, Complex):
            return Complex(self.nbr * nbr.r, self.nbr * nbr.i)

    def div(self, nbr):
        if isinstance(nbr, Rationels):
            res = self.nbr / nbr.nbr
            return Rationels(res)
        if isinstance(nbr, Complex):
            haut = Complex(nbr.r, -nbr.i).mult(self)
            bas = nbr.mult(Complex(nbr.r, -nbr.i))
            return haut.div(Rationels(bas.r))

    def mod(self, nbr):
        if isinstance(nbr, Rationels):
            res = self.nbr % nbr.nbr
            return Rationels(res)
        if isinstance(nbr, Complex):
            return "Error"

    def pow(self, nbr):
        if isinstance(nbr, Rationels):
            res = ft_pow(self.nbr, nbr.nbr)
            return Rationels(res)
        if isinstance(nbr, Complex):
            return Complex(self.nbr - nbr.r, nbr.i)


class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

    def __str__(self):
        str_r = str(self.r)
        str_i = str(self.i)
        return str_r + ' + ' + str_i + 'i '

    def to_str(self):
        str_r = str(self.r)
        str_i = str(self.i)
        return str_r + ' + ' + str_i + 'i '

    def add(self, nbr):
        if isinstance(nbr, Rationels):
            r = self.r + nbr.nbr
            return Complex(r, self.i)
        if isinstance(nbr, Complex):
            r = self.r + nbr.r
            i = self.i + nbr.i
            return Complex(r, i)

    def sous(self, nbr):
        if isinstance(nbr, Rationels):
            r = self.r - nbr.nbr
            return Complex(r, self.i)
        if isinstance(nbr, Complex):
            r = self.r - nbr.r
            i = self.i - nbr.i
            return Complex(r, i)

    def mult(self, nbr):
        if isinstance(nbr, Rationels):
            r = self.r + nbr.nbr
            i = self.i + nbr.nbr
            return Complex(r, i)
        if isinstance(nbr, Complex):
            r = self.r * nbr.r + self.i * nbr.i * -1
            i = self.r * nbr.i + self.i * nbr.r
            return Complex(r, i)

    def div(self, nbr):
        if isinstance(nbr, Rationels):
            r = self.r / nbr.nbr
            i = self.i / nbr.nbr
            return Complex(r, i)
        if isinstance(nbr, Complex):
            haut = Complex(nbr.r, -nbr.i).mult(self)
            bas = Complex(nbr.r, -nbr.i).mult(nbr)
            return haut.div(Rationels(bas.r))

    def mod(self, nbr):
        return "Error"

    def pow(self, nbr):
        if isinstance(nbr, Rationels):
            base = Complex(self.r, self.i)
            res = Complex(self.r, self.i)
            while nbr.nbr > 1:
                res = res.mult(base)
                nbr.nbr -= 1
            return res
        if isinstance(nbr, Complex):
            return "Error"


class Matrice:
    def __init__(self, nbr):
        self.r = 0