import re
import random


variables = {"rationel": {"a": 25, "po": 12}, "complexe": {"tagada": "pilou"}, "matrices": {}}

class Rationels:
    def __init__(self, nbr):
        self.nbr = nbr
        self.is_positif = True if nbr >= 0 else False

    def __repr__(self):
        return self.nbr

    def __str__(self):
        return str(self.nbr)

nbr = Rationels(23)
nbr2 = 23
print(isinstance(nbr, basestring))
print(isinstance(nbr2, Rationels))



if "a" in variables["rationel"]:
    print("Ok")

if "b" in variables["rationel"]:
    print("Not Ok")

print '----------------------------'

func = 'func(54896+689/5*(3+2))'
index = 4
print(func[:4] + '*' + func[4:])
