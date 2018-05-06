from math_func import ft_pow


class Rationels:
    def __init__(self, nbr):
        self.nbr = nbr
        self.is_positif = True if nbr >= 0 else False

    def __str__(self):
        return str(self.nbr)

    def add(self, nbr):
        if isinstance(nbr, Rationels):
            self.nbr += nbr.nbr
            return self
        if isinstance(nbr, Complex):
            return Complex(self.nbr + nbr.r, nbr.i)

    def sous(self, nbr):
        if isinstance(nbr, Rationels):
            self.nbr -= nbr.nbr
            return self
        if isinstance(nbr, Complex):
            return Complex(self.nbr - nbr.r, nbr.i)

    def mult(self, nbr):
        if isinstance(nbr, Rationels):
            self.nbr *= nbr.nbr
            return self
        if isinstance(nbr, Complex):
            return Complex(self.nbr * nbr.r, self.nbr * nbr.i)

    def div(self, nbr):
        if isinstance(nbr, Rationels):
            self.nbr /= nbr.nbr
            return self
        if isinstance(nbr, Complex):
            haut = Complex(nbr.r, -nbr.i).mult(self.nbr)
            bas = nbr.mult(Complex(nbr.r, -nbr.i))
            return haut.div(Rationels(bas.r))

    def mod(self, nbr):
        if isinstance(nbr, Rationels):
            self.nbr %= nbr.nbr
            return self
        if isinstance(nbr, Complex):
            return "Error"

    def pow(self, nbr):
        if isinstance(nbr, Rationels):
            self.nbr = ft_pow(self.nbr, nbr.nbr)
            return self
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

    def add(self, nbr):
        if isinstance(nbr, Rationels):
            self.r += nbr.nbr
            return self
        if isinstance(nbr, Complex):
            self.r += nbr.r
            self.i += nbr.i
            return self

    def sous(self, nbr):
        if isinstance(nbr, Rationels):
            self.r -= nbr.nbr
            return self
        if isinstance(nbr, Complex):
            self.r -= nbr.r
            self.i -= nbr.i
            return self

    def mult(self, nbr):
        if isinstance(nbr, Rationels):
            self.r *= nbr.nbr
            self.i *= nbr.nbr
            return self
        if isinstance(nbr, Complex):
            self.r = self.r * nbr.r + self.i * nbr.i * -1
            self.i -= self.r * nbr.i + self.i * nbr.r
            return self

    def div(self, nbr):
        if isinstance(nbr, Rationels):
            self.r /= nbr.nbr
            self.i /= nbr.nbr
            return self
        if isinstance(nbr, Complex):
            haut = Complex(nbr.r, -nbr.i).mult(self)
            bas = Complex(nbr.r, -nbr.i).mult(nbr)
            return haut.div(Rationels(bas.r))

    def mod(self, nbr):
        return "Error"

    def pow(self, nbr):
        if isinstance(nbr, Rationels):
            base = self
            res = self
            while nbr.nbr > 1:
                res = self.mult(base)
                nbr.nbr -= 1
            return res
        if isinstance(nbr, Complex):
            return "Error"
