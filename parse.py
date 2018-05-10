# -*- coding: utf-8 -*-
import re


def extract_matrice(input):
    regex = "^\[\[[-0-9.]+(,[-0-9.]+)*\](;\[[-0-9.]+(,[-0-9.]+)*\])*\]"
    match = re.search(regex, input)
    if match is not None:
        return match.group(0)
    else:
        if input.count('[') > 0:
            print "Matrice mal formatée"
        return None

def extract_function(input):
    regex = "^[a-z]+\((.+)\)"
    if not re.match(regex, input):
        return None
    index = input.find('(')
    bracket_count = 0
    while index < len(input):
        if input[index] == '(':
            bracket_count += 1
        elif input[index] == ')':
            bracket_count -= 1
        if bracket_count == 0:
            break
        index += 1
    return input[:index + 1]


def extract_nbr(input):
    regex = "^\-?[0-9]+(\.[0-9]+)?"
    match = re.search(regex, input)
    if match is not None:
        return match.group(0)
    else:
        return None


def extract_var(input):
    regex = "^[a-z]+"
    match = re.search(regex, input)
    if match is not None:
        return match.group(0)
    else:
        return None


def to_tab(input):
    nbr = True
    index = 0 #gestion des erreurs un nbr puis un signe etc
    token_list = []
    while index < len(input):
        if nbr:
            if extract_function(input[index:]):
                tmp = extract_function(input[index:])
                token_list.append([3, tmp])
                index += len(tmp)
                nbr = False
            elif extract_var(input[index:]):
                tmp = extract_var(input[index:])
                token_list.append([2, tmp])
                index += len(tmp)
                nbr = False
            elif extract_matrice(input[index:]):
                tmp = extract_matrice(input[index:])
                token_list.append([2, tmp])
                index += len(tmp)
                nbr = False
            elif extract_nbr(input[index:]):
                tmp = extract_nbr(input[index:])
                token_list.append([1, tmp])
                index += len(tmp)
                nbr = False
            elif input[index] == '(':
                token_list.append([4, '('])
                index += 1
            else:
                print "can't recognize token near %s" % input[index-3 if index-3 >= 0 else 0:index+2]
                return "error"
        else:
            match = re.match(r'\*\*|[\-+/^%=*]', input[index])
            if match is not None:
                token_list.append([0, match.group(0)])
                index += len(match.group(0))
                nbr = True
            elif input[index] == ')':
                token_list.append([5, ')'])
                index += 1
            elif input[index] == 'i':
                token_list.append([0, '*'])
                token_list.append([2, 'i'])
                index += 1
                nbr = False
            else:
                print "can't recognize token near %s" % input[index-3 if index-3 >= 0 else 0:index+2]
                return "error"
    print('token_list')
    print(token_list)
    return token_list


def parse(input):
    function_regex = re.compile('^([a-z]+)\((.+)\)=')
    parse_info = {'assign': False, 'assign_func': False, 'resolve_equat': False, 'error': False}
    if not input:
        parse_info['error'] = True
        print('Error: Empty input')
        return parse_info
    if not input.endswith('?'):
        parse_info['assign'] = True
        match = re.match(function_regex, input)
        if match is not None:
            tmp = extract_function(input)
            parse_info['assign_func'] = match.group(1)
            parse_info['var'] = match.group(2)
            if input[len(tmp)] != "=":
                print("Error: assign")
                parse_info['error'] = True
        elif input[0].isalpha():
            tmp = extract_var(input)
            parse_info['assign'] = tmp
            if input[len(tmp)] != "=":
                print("Error: assign")
                parse_info['error'] = True
        else:
            print("Error assign")
            parse_info['error'] = True
    elif not input.endswith('=?'):
        parse_info['resolve_equat'] = True
    if input.count("=") > 1:
        print("Error: more than one equal")
        parse_info['error'] = True
    return parse_info
