import re


def extract_function(input, index):
    func = ""
    first_bracket = 0
    last_bracket = 0
    while index < len(input) and (first_bracket == 0 or first_bracket != last_bracket):
        if input[index] == "(":
            first_bracket += 1
        if input[index] == ")":
            last_bracket += 1
        func += input[index]
        index += 1
    return func


def extract_nbr(input, index):
    nbr = ""
    while index < len(input) and input[index].isdigit():
        nbr += input[index]
        index += 1
    return nbr


def extract_var(input, index):
    var = ""
    while index < len(input) and input[index].isalpha():
        var += input[index]
        index += 1
    return var


def to_tab(input):
    function_regex = re.compile('^[a-z]+\(')
    index = 0 #gestion des erreurs un nbr puis un signe etc
    token_list = []
    while index < len(input):
        if re.match(function_regex, input[index:],):
            tmp = extract_function(input, index)
            index += len(tmp)
            token_list.append(tmp)
        elif input[index].isalpha():
            tmp = extract_var(input, index)
            index += len(tmp)
            token_list.append(tmp)
        elif input[index].isdigit():
            tmp = extract_nbr(input, index)
            index += len(tmp)
            token_list.append(tmp)

        else:
            token_list.append(input[index])
            index += 1
    return token_list

def shunting_yard(input):
    if re.match(r'^[a-z]+=', input):
        var = extract_var(input, 0)
        input = re.sub(r'^[a-z]+=', '', input).lower()
        token_list = to_tab(input)
        print(token_list)
    elif re.match(r'=?$', input):
        is_result_calc = True
        input = re.sub(r'=?$', '', input).lower()
        token_list = to_tab(input)
        print(token_list)
    else:
        return 'problem'


def parse_all(input):
    function_regex = re.compile('^[a-z]+\(')
    index = 0
    parse_info = {'nbr': True, 'assign': None, 'equal': False, 'assign_func': False}
    if not input.endswith('?'):
        parse_info['assign'] = True
    while index < len(input):
        if re.match(function_regex, input[index:]):
            if parse_info['nbr'] == False:
                print('Erreur: Excepected Number or variable')
            if index == 0 and parse_info['assign']:
                tmp = extract_function(input, 0)
                index += len(tmp)
                parse_info['assign_func'] = tmp
            else
        if input[index] == 'i':
            index += 1
            parse_info['nbr'] = False
        elif input[index].isalpha():
            return 1


def parsing(input):
    parse_all(input)



    function_regex = re.compile('^[a-z]+\([a-z]\)')
    if re.match(function_regex, input):
        ftnftn = 0
    else:
        shunting_yard(input)

