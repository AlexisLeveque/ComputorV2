import re


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
    if re.match(complex_regex , equat):
        print "Error can't have complex in equation"
    while re.match(function_regex, equat):
        match = re.match(function_regex, equat)
        func_name = match.group(1)
        func_var = match.group(2)
        function = variables['function'][func_name]
        equat = equat.replace(match.group(0), function.func.replace(function.var, func_var))
    while re.match(var_regex, equat):










def parse_equat(equat, variables):
    replace_var(equat, variables)
    simpler = add_one_before_x(equat)
    print(simpler)
    same_sided = move_to_the_same_side(simpler)
    return same_sided


parse_equat("35x^2+8-25x=ax-trib+x+f(3+5)")


# replace var et fonction par leur valeur tant qu'on en a .
# reduire les parenthese
# resoudre
