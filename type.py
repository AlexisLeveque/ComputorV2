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
        if isinstance(nbr, Matrice):
            res_matrice = []
            lign_index = 0
            while lign_index < nbr.lign:
                res_matrice.append([])
                col_index = 0
                while col_index < nbr.column:
                    res_matrice[lign_index].append(Rationels(nbr.matrice[lign_index][col_index].nbr + self.nbr))
                    col_index += 1
                lign_index += 1
            return Matrice(res_matrice, nbr.lign, nbr.column)


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
    def __init__(self, matrice, lign, column):
        self.column = column
        self.lign = lign
        self.matrice = matrice

    def __str__(self):
        lign_index = 0
        while lign_index < self.lign:
            col_index = 0
            print '[',
            while col_index < self.column:
                print " " + str(self.matrice[lign_index][col_index]) + " ",
                col_index += 1
                if col_index < self.column:
                    print ",",
            print ']'
            lign_index += 1
        return ''
