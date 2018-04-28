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
    while index < len(input) and (input[index].isdigit() or input[index] == "."):
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
    parse_info = {'nbr': None, 'assign': None, 'equal': False, 'assign_func': False, "error": False}
    if not input.endswith('?'):
        parse_info['assign'] = True#check first is a variable tho
    while index < len(input):
        if re.match(function_regex, input[index:]):
            if parse_info['nbr'] == False:
                print 'Error: Excepected Operator near \"%s\"' % input[index-3:index+2]
                parse_info['error'] = True
                return parse_info
            if index == 0 and parse_info['assign'] is not None:
                tmp = extract_function(input, 0)
                index += len(tmp)
                parse_info['assign_func'] = tmp
                parse_info['nbr'] = False
            else:
                index += len(extract_function(input, index))
                parse_info['nbr'] = False
        elif input[index].isalpha():
            tmp = extract_var(input, index)
            if tmp == "x" and index == 0 and parse_info['assign'] == True:
                parse_info['assign'] = 'x'
                index += 1
                parse_info['nbr'] = False
            elif tmp == "i" or tmp == 'x':
                index += 1
                parse_info['nbr'] = False
            elif parse_info['nbr'] == False:
                print 'Error: Excepected Operator near \"%s\"' % input[index-3:index+2]
                parse_info['error'] = True
                return parse_info
            elif index == 0 and parse_info['assign'] is not None:
                parse_info['nbr'] = False
                parse_info['assign'] = tmp
                index += len(tmp)
            else:
                parse_info['nbr'] = False
                index += len(tmp)
        #ismatrice
        elif input[index].isdigit():
            if parse_info['nbr'] == False:
                print 'Error: Excepected Operator near \"%s\"' % input[index-3:index+2]
                parse_info['error'] = True
                return parse_info
            else:
                parse_info['nbr'] = False
                index += len(extract_nbr(input, index))
        elif re.match(r'[+\-*/^%=]', input[index]):
            if input[index] == '-':
                parse_info['nbr'] = False
            if parse_info['nbr'] == True:
                print "Error: Excepected Number or variable near \"%s\"" % input[index-3:index+2]
                parse_info['error'] = True
                return parse_info
            elif input[index] == '=' and parse_info['equal'] == True:
                print 'Error: Unexpected = near \"%s\"' % input[index-3:index+2]
                parse_info['error'] = True
            elif input[index] == '=':
                parse_info['equal'] = True
                index += 1
                parse_info['nbr'] = None
            else:
                index += 1
                parse_info['nbr'] = True
        else:
            index +=1
        if parse_info['error'] == True:
            return parse_info
    if parse_info['error'] == False and parse_info['assign'] == True and parse_info['assign_func'] == False:
        print("Error: No variable to assign")
        parse_info['error'] = True
    return parse_info


def parse(input):
    function_regex = re.compile('^[a-z]+\(')
    parse_info = {'assign': False, 'assign_func': False, "error": False}
    if not input.endswith('?'):
        parse_info['assign'] = True
        if re.match(function_regex, input[0]):
            tmp = extract_function(input, 0)
            parse_info['assign_func'] = tmp
            if input[len(tmp)] != "=":
                print("Error: assign")
                parse_info['error'] = True
        elif input[0].isalpha():
            tmp = extract_var(input, 0)
            parse_info['assign'] = tmp
            if input[len(tmp)] != "=":
                print("Error: assign")
                parse_info['error'] = True
        else:
            print("Error assign")
            parse_info['error'] = True
    if input.count("=") > 1:
        print("Error: more than one equal")
        parse_info['error'] = True


def parsing(input):
    print(parse(input))

    function_regex = re.compile('^[a-z]+\([a-z]\)')
    if re.match(function_regex, input):
        ftnftn = 0
    else:
        shunting_yard(input)

