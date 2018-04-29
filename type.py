import re


def extract_function(input):
    regex = "^[a-z]+\(.*\)"
    match = re.search(regex, input)
    if match is not None:
        return match.group(0)
    else:
        return None


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
                token_list.append(tmp)
                index += len([2, tmp])
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
                print "can't recognize token near %s" % input[index-3:index+2]
        else:
            match = re.match(r'[+\-*/^%=]', input[index])
            if match is not None:
                token_list.append([0, match.group(0)])
                index += 1
                nbr = True
            elif input[index] == ')':
                token_list.append([5, ')'])
                index += 1
            else:
                print "can't recognize token near %s" % input[index-3:index+2]
    return token_list


def greater_precedence(operator1, operator2):
    if operator1 == '^':
        return False
    if operator1 == '*' or operator1 == '/' or operator1 == '%':
        if operator2 == '^':
            return True
        else:
            return False
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
        elif  tokens[index][0] == '(':
            operator.append('(')
        elif tokens[index][0] == ')':
            op_index = len(operator) - 1
            while len(operator) and operator[op_index] != '(':
                output.append(operator.pop())
            if not len(operator):
                print("Error parenthesage")
            else:
                operator.pop()
        index += 1
    while len(operator):
        output.append(operator.pop())
    return output


def resolve(input):
    print('there')
    if re.match(r'^[a-z]+=', input):
        var = extract_var(input)
        input = re.sub(r'^[a-z]+=', '', input).lower()
        token_list = to_tab(input)
        print(token_list)
    elif input.endswith("=?"):
        is_result_calc = True
        print('here')
        token_list = to_tab(input[:-2])
        print shunting_yard(token_list)
    else:
        return 'problem'


def parse(input):
    function_regex = re.compile('^[a-z]+\(')
    parse_info = {'assign': False, 'assign_func': False, 'resolve_equat': False, 'error': False}
    if not input.endswith('?'):
        parse_info['assign'] = True
        if re.match(function_regex, input[0]):
            tmp = extract_function(input)
            parse_info['assign_func'] = tmp
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


def parsing(input):
    parse_info = parse(input)
    if parse_info['error'] == True:
        return "Error"

    # if parse_info['assign_func']:
    #     resolve_func()
    # elif parse_info['assign']:
    #     assign_resolve()
    # elif parse_info['resolve_equat']:
    #     resolve_equat()
    # else:
    resolve(input)



# def parse_all(input):
#     function_regex = re.compile('^[a-z]+\(')
#     index = 0
#     parse_info = {'nbr': None, 'assign': None, 'equal': False, 'assign_func': False, "error": False}
#     if not input.endswith('?'):
#         parse_info['assign'] = True#check first is a variable tho
#     while index < len(input):
#         if re.match(function_regex, input[index:]):
#             if parse_info['nbr'] == False:
#                 print 'Error: Excepected Operator near \"%s\"' % input[index-3:index+2]
#                 parse_info['error'] = True
#                 return parse_info
#             if index == 0 and parse_info['assign'] is not None:
#                 tmp = extract_function(input, 0)
#                 index += len(tmp)
#                 parse_info['assign_func'] = tmp
#                 parse_info['nbr'] = False
#             else:
#                 index += len(extract_function(input, index))
#                 parse_info['nbr'] = False
#         elif input[index].isalpha():
#             tmp = extract_var(input, index)
#             if tmp == "x" and index == 0 and parse_info['assign'] == True:
#                 parse_info['assign'] = 'x'
#                 index += 1
#                 parse_info['nbr'] = False
#             elif tmp == "i" or tmp == 'x':
#                 index += 1
#                 parse_info['nbr'] = False
#             elif parse_info['nbr'] == False:
#                 print 'Error: Excepected Operator near \"%s\"' % input[index-3:index+2]
#                 parse_info['error'] = True
#                 return parse_info
#             elif index == 0 and parse_info['assign'] is not None:
#                 parse_info['nbr'] = False
#                 parse_info['assign'] = tmp
#                 index += len(tmp)
#             else:
#                 parse_info['nbr'] = False
#                 index += len(tmp)
#         #ismatrice
#         elif input[index].isdigit():
#             if parse_info['nbr'] == False:
#                 print 'Error: Excepected Operator near \"%s\"' % input[index-3:index+2]
#                 parse_info['error'] = True
#                 return parse_info
#             else:
#                 parse_info['nbr'] = False
#                 index += len(extract_nbr(input, index))
#         elif re.match(r'[+\-*/^%=]', input[index]):
#             if input[index] == '-':
#                 parse_info['nbr'] = False
#             if parse_info['nbr'] == True:
#                 print "Error: Excepected Number or variable near \"%s\"" % input[index-3:index+2]
#                 parse_info['error'] = True
#                 return parse_info
#             elif input[index] == '=' and parse_info['equal'] == True:
#                 print 'Error: Unexpected = near \"%s\"' % input[index-3:index+2]
#                 parse_info['error'] = True
#             elif input[index] == '=':
#                 parse_info['equal'] = True
#                 index += 1
#                 parse_info['nbr'] = None
#             else:
#                 index += 1
#                 parse_info['nbr'] = True
#         else:
#             index +=1
#         if parse_info['error'] == True:
#             return parse_info
#     if parse_info['error'] == False and parse_info['assign'] == True and parse_info['assign_func'] == False:
#         print("Error: No variable to assign")
#         parse_info['error'] = True
#     return parse_info

