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
            match = re.match(r'[+\-*/^%=]', input[index])
            if match is not None:
                token_list.append([0, match.group(0)])
                index += 1
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
    function_regex = re.compile('^[a-z]+\(')
    parse_info = {'assign': False, 'assign_func': False, 'resolve_equat': False, 'error': False}
    if not input:
        parse_info['error'] = True
        print('Error: Empty input')
        return parse_info
    if not input.endswith('?'):
        parse_info['assign'] = True
        if re.match(function_regex, input):
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

