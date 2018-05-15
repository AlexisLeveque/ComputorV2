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


def parse_equat(equat):
    simpler = add_one_before_x(equat)
    print(simpler)
    same_sided = move_to_the_same_side(simpler)
    return same_sided


parse_equat("35x^2+8-25x=ax-trib+x+f(3+5)")