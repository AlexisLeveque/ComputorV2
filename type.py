from math_func import ft_pow


class Rationels:
    def __init__(self, nbr):
        self.nbr = nbr
        self.is_positif = True if nbr >= 0 else False

    def add(self, nbr):
        if type(nbr, Rationels):
            self.nbr += nbr
            return self
        if type(nbr, Complex):
            return Complex(self.nbr + nbr.r, nbr.i)

    def sous(self, nbr):
        if type(nbr, Rationels):
            self.nbr -= nbr
            return self
        if type(nbr, Complex):
            return Complex(self.nbr - nbr.r, nbr.i)

    def mult(self, nbr):
        if type(nbr, Rationels):
            self.nbr *= nbr
            return self
        if type(nbr, Complex):
            return Complex(self.nbr * nbr.r, self.nbr * nbr.i)

    def div(self, nbr):
        if type(nbr, Rationels):
            self.nbr /= nbr
            return self
        if type(nbr, Complex):
            return Complex(self.nbr - nbr.r, nbr.i) #galeeeeeere

    def mod(self, nbr):
        if type(nbr, Rationels):
            self.nbr %= nbr
            return self
        if type(nbr, Complex):
            return "Error"

    def pow(self, nbr):
        if type(nbr, Rationels):
            self.nbr = ft_pow(self.nbr, nbr)
            return self.nbr
        if type(nbr, Complex):
            return Complex(self.nbr - nbr.r, nbr.i)


class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

    def add(self, nbr):
        if type(nbr, Rationels):
            self.r += nbr
            return self
        if type(nbr, Complex):
            self.r += nbr.r
            self.i += nbr.i
            return self

    def sous(self, nbr):
        if type(nbr, Rationels):
            self.r -= nbr
            return self
        if type(nbr, Complex):
            self.r -= nbr.r
            self.i -= nbr.i
            return self

    def mult(self, nbr):
        if type(nbr, Rationels):
            self.r *= nbr
            self.i *= nbr
            return self
        if type(nbr, Complex):
            self.r = self.r * nbr.r + self.i * nbr.i * -1
            self.i -= self.r * nbr.i + self.i * nbr.r
            return self

    def div(self, nbr):
        if type(nbr, Rationels):
            self.r /= nbr
            self.i /= nbr
            return self
        if type(nbr, Complex):
            return Complex(self.nbr - nbr.r, nbr.i) #galeeeeeere

    def mod(self, nbr):
        return "Error"

    def pow(self, nbr):
        if type(nbr, Rationels):
            base = self
            res = self
            while nbr > 1:
                res = self.mult(base)
                nbr -= 1
            return res
        if type(nbr, Complex):
            return "Error"
