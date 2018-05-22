import re
from resolve import shunting_yard
from type import Rationels, Function, Inconnue
from parse import extract_var, extract_function, to_tab


def types(nbr):
    nbr_regex = re.compile('^-?[0-9]+(\.[0-9]+)?')
    if isinstance(nbr, Rationels) or isinstance(nbr, Inconnue):
        return nbr
    if nbr == 'x':
        nbr = Inconnue(1, 1)
    elif re.match(nbr_regex, nbr):
        nbr = Rationels(float(nbr))
    else:
        print "Error: can't recognise this thing"
    return nbr


def calc(nbr1, nbr2, operator):
    nbr1 = types(nbr1)
    nbr2 = types(nbr2)
    if operator == '+':
        if isinstance(nbr2, Inconnue):
            return nbr2.add(nbr1)
        return nbr1.add(nbr2)
    elif operator == '-':
        if isinstance(nbr2, Inconnue):
            return nbr2.sous(nbr1, 1)
        return nbr1.sous(nbr2)
    elif operator == '*':
        if isinstance(nbr2, Inconnue):
            return nbr2.mult(nbr1)
        return nbr1.mult(nbr2)
    elif operator == '/':
        if isinstance(nbr2, Inconnue):
            nbr2.div(nbr1, 1)
        return nbr1.div(nbr2)
    elif operator == '%':
        if isinstance(nbr2, Inconnue):
            nbr2.mod(nbr1)
        return nbr1.mod(nbr2)
    elif operator == '^':
        if isinstance(nbr2, Inconnue):
            nbr2.pow(nbr1, 1)
        return nbr1.pow(nbr2)
    elif operator == '**':
        print("Error: can't have ** operator")


def npi(input):
    index = 0
    if len(input) == 1:
        return input[0]
    while len(input) > 1:
        if isinstance(input[index], basestring) and re.match(r'^\*\*|[\-+/^%=*]$', input[index]):
            res = calc(input[index-2], input[index-1], input[index])
            input[index] = res
            input.pop(index - 1)
            input.pop(index - 2)
            index = 0
        index += 1
    return input[0]


def reduction(equat):
    print("tab")
    first_part = equat.split('=')[0]
    tab = to_tab(first_part)
    shun = shunting_yard(tab)
    inp = npi(shun)
    return "8"

def parenthesis(equat):
    index = 0
    parenthese = -1
    parentheses_start = 0
    while index < len(equat):
        if equat[index] == ')':
            if parenthese == -1:
                print("Error: parenthese")
            else:
                parenthese -= 1
                if parenthese == 0:
                    parenthese = -1
                    res = parenthesis(equat[parentheses_start + 1:index])
                    equat = equat.replace(equat[parentheses_start:index+1], res)
                    index = 0
        if equat[index] == '(':
            if parenthese == -1:
                parentheses_start = index
                parenthese = 1
            else:
                parenthese += 1
        index += 1
    return reduction(equat)


def add_multiplication(input):
    index = 0
    number = False
    while index < len(input):
        if input[index].isalpha() and number:
            input = input[:index] + '*' + input[index:]
        if input[index].isdigit():
            number = True
        else:
            number = False
        index += 1
    return input


def add_to_tab(expr,  inverse):
  print(expr)


def move_to_the_same_side(expr):
    tab = []
    inverse = False
    last_sign = 0
    index = 1
    while index < len(expr):
        if expr[index] == '=':
            inverse = True
        if expr[index] == '+' or expr[index] == '-' or expr[index] == '=':
            tab.append(add_to_tab(expr[last_sign: index], inverse))
            last_sign = index
        index += 1
    tab.append(add_to_tab(expr[last_sign: index], inverse))


def add_one_before_x(equat):
    if equat.startswith('x'):
        expr = '1'+equat
    return equat.replace('-x', '-1x').replace('+x', '+1x')


def replace_var(equat, variables):
    complex_regex = "[^a-z]i[^a-z]|^i[^a-z]|[^a-z]i$"
    function_regex = "([a-z]+)\((.+)\)"
    var_regex = "[a-z]+"
    if re.match(complex_regex, equat):
        print "Error can't have complex in equation"
    index = 0
    while index < len(equat):
        if equat[index].isalpha():
            if extract_function(equat[index:]):
                func_regex = re.compile('^([a-z]+)\((.+)\)')
                match = re.match(func_regex, equat[index:])
                if match is not None:
                    name = match.group(1)
                    calc = '(' + match.group(2) + ')'

                    function = variables["function"][name]
                    equat = equat.replace(match.group(0), function.func.replace(function.var, calc))
                index = 0
            else:
                var = extract_var(equat[index:])
                if var != 'x':
                    nbr = ""
                    if var in variables["rationel"]:
                        nbr = variables["rationel"][var]
                        nbr = str(nbr.nbr)
                    elif var in variables["complexe"]:
                        print "Error can't have complex in equation"
                    elif var in variables["matrices"]:
                        print "Error Can't have matrice in second degree equation"
                    else:
                        print("Error: var not defined %s" % var)
                    equat = equat.replace(var, nbr).replace(' ', '')
                    index = 0
        index += 1
    print("equat:")
    print(equat)
    return equat


def parse_equat(equat, variables):
    r = replace_var(equat, variables)
    simpler = add_multiplication(add_one_before_x(r))
    print(simpler)
    parenthesis(simpler)
    same_sided = move_to_the_same_side(simpler)
    return same_sided


variables = {"rationel": {"trib": Rationels(21), "ax": Rationels(2)}, "complexe": {}, "matrices": {}, "function": {'f': Function('x^2 + trib', 'x')}}
print("35x^2+8-25x=ax-trib+x+f(3+5)")
parse_equat("35x^2+8-25x=ax-trib+x+f(3+5)", variables)


# replace var et fonction par leur valeur tant qu'on en a .
# reduire les parenthese
# resoudre
