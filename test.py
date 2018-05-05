import re
import random


variables = {"rationel": {"a": 25, "po": 12}, "complexe": {"tagada": "pilou"}, "matrices": {}}

class Rationels:
    def __init__(self, nbr):
        self.nbr = nbr
        self.is_positif = True if nbr >= 0 else False


nbr = Rationels(23)

print(type(nbr, Rationels))
if "a" in variables["rationel"]:
    print("Ok")

if "b" in variables["rationel"]:
    print("Not Ok")