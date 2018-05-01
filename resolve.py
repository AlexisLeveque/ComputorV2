# -*- coding: utf-8 -*-
import re
from parse import to_tab, extract_var, extract_nbr, extract_function, parse

variables = {"rationel": {}, "complexe": {}, "matrices": {}}

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
    if re.match(r'^[a-z]+=', input):
        input = re.sub(r'^[a-z]+=', '', input).lower()
        token_list = to_tab(input)
        return shunting_yard(token_list)
    elif input.endswith("=?"):
        token_list = to_tab(input[:-2])
        return shunting_yard(token_list)

    else:
        return 'problem'



def resolve_equat(input):
    return 0#parse equation and enter it



def resolve_func(input, parse_info):
    return 0#appeller mon (second degrée auquel il faut rajouter les (8X)


def assign_resolve(input, parse_info):
    var = extract_var(input)
    resolve(input)
    return 0


def parsing(input):
    parse_info = parse(input)
    print(variables)
    if parse_info['error'] == True:
        return "Error"

    if parse_info['assign_func']:
        resolve_func(input, parse_info)
    elif parse_info['assign']:
        assign_resolve(input, parse_info)
    elif parse_info['resolve_equat']:
        resolve_equat(input)
    else:
        print(resolve(input))
    print("parse_info")
    print(parse_info)