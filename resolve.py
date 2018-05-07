# -*- coding: utf-8 -*-
import re
from parse import to_tab, extract_var, extract_nbr, extract_function, parse
from type import Complex, Rationels

variables = {"rationel": {}, "complexe": {}, "matrices": {}}


def recup_var(var):
    if var in variables["rationel"]:
        return variables["rationel"][var]
    elif var in variables["complexe"]:
        return variables["complexe"][var]
    elif var in variables["matrices"]:
        return variables["matrices"][var]
    else:
        print("Error")


def type(nbr):
    function_regex = re.compile('^[a-z]+\(')
    nbr_regex = re.compile('^-?[0-9]+(\.[0-9]+)?')
    if isinstance(nbr, Rationels) or isinstance(nbr, Complex):
        return nbr
    if nbr == 'i':
        nbr = Complex(0, 1)
    elif re.match(function_regex, nbr):
        nbr = resolve_func(nbr)
    elif nbr.isalpha():
        nbr = recup_var(nbr)
    elif re.match(nbr_regex, nbr):
        nbr = Rationels(int(nbr))
    return nbr


def calc(nbr1, nbr2, operator, input):
    nbr1 = type(nbr1)
    nbr2 = type(nbr2)
    if operator == '+':
        return nbr1.add(nbr2)
    elif operator == '-':
        return nbr1.sous(nbr2)
    elif operator == '*':
        return nbr1.mult(nbr2)
    elif operator == '/':
        return nbr1.div(nbr2)
    elif operator == '%':
        return nbr1.mod(nbr2)
    elif operator == '^':
        return nbr1.pow(nbr2)


def npi_solver(input):
    index = 0
    if len(input) == 1:
        input[0] = type(input[0])
    while len(input) > 1:
        if isinstance(input[index], basestring) and re.match(r'[+\-*/^%=]', input[index]):
            res = calc(input[index-2], input[index-1], input[index], input)
            input[index] = res
            input.pop(index - 1)
            input.pop(index - 2)
            index = 0
        index += 1
    return input[0]


def greater_precedence(operator1, operator2):
    if operator2 == '(':
        return False
    if operator1 == '^':
        return False
    if operator1 == '*' and operator2 == '/':
        return True
    if operator1 == '*' or operator1 == '/' or operator1 == '%':
        if operator2 == '^':
            return True
        else:
            return False
    if operator1 == '+' and operator2 == '-':
        return True
    if operator1 == '-' or operator1 == '+':
        if operator2 == '-' or operator2 == '+':
            return False
        else:
            return True


def shunting_yard(tokens):
    operator = []
    output = []
    index = 0
    while index < len(tokens):
        if 4 > tokens[index][0] > 0:
            output.append(tokens[index][1])
        elif tokens[index][0] == 0:
            op_index = len(operator)-1
            while len(operator) and greater_precedence(tokens[index][1], operator[op_index]):
                output.append(operator.pop())
                op_index -= 1
            operator.append(tokens[index][1])
        elif tokens[index][0] == 4:
            operator.append('(')
        elif tokens[index][0] == 5:
            op_index = len(operator) - 1
            while len(operator) and operator[op_index] != '(':
                output.append(operator.pop())
                op_index -= 1
            if not len(operator):
                print("Error parentesage")
            else:
                operator.pop()
        index += 1
    while len(operator):
        output.append(operator.pop())
    return output


def resolve(input):
    if input.endswith("=?"):
        token_list = to_tab(input[:-2])
        shun = shunting_yard(token_list)
        return npi_solver(shun)
    elif re.match(r'^[a-z]+=', input):
        input = re.sub(r'^[a-z]+=', '', input)
        token_list = to_tab(input)
        shun = shunting_yard(token_list)
        return npi_solver(shun)
    else:
        return 'problem'



def resolve_equat(input):

    return 0#appeller mon second degrée auquel il faut rajouter les (8X)



def assign_func(input, parse_info):
    return 0#parse equation and enter it


def assign_resolve(input, parse_info):
    var = parse_info["assign"]
    res = resolve(input)
    if var in variables["rationel"]:
        variables["rationel"].pop(var)
    if var in variables["complexe"]:
        variables["complexe"].pop(var)
    if isinstance(res, Rationels):
        variables["rationel"][var] = res
    if isinstance(res, Complex):
        variables["complexe"][var] = res
    print(res)
    return 0


def parsing(input):
    parse_info = parse(input)
    print(variables)
    if parse_info['error'] == True:
        return "Error"

    if parse_info['assign_func']:
        assign_func(input, parse_info)
    elif parse_info['assign']:
        assign_resolve(input, parse_info)
    elif parse_info['resolve_equat']:
        resolve_equat(input)
    else:
        res = resolve(input)
        print('--------------------------------------------------')
        print res
        print('--------------------------------------------------')

    # print("parse_info")
    # print(parse_info)