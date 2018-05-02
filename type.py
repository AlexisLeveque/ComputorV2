class Rationels:
    def __init__(self, nbr):
        self.nbr = nbr
        self.is_positif = True if nbr >= 0 else False



class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
