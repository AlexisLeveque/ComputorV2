import re


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
    index = 0 #gestion des erreurs un nbr puis un signe etc
    token_list = []
    while index < len(input):
        if input[index].isalpha():
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

def parsing(input):
    function_regex = re.compile('^[a-z]+\([a-z]\)')
    if re.match(function_regex, input):
        ftnftn = 0
    else:
        shunting_yard(input)


#https://brilliant.org/wiki/shunting-yard-algorithm/