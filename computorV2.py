# -*- coding: utf-8 -*-
import sys
import re
from resolve import parsing


def add_multiplication(input):
    index = 0
    number = False
    while index < len(input):
        if input[index].isalpha() and number:
            input = input[:index] + '*' + input[index:]
        if input[index].isdigit():
            number = True
        else:
            number = False
        index += 1
    return input


while 1:
    input = raw_input('> ')
    input = re.sub(r'[ \t]', '', input).lower() # rajouter un * si on a des chiffres puis des lettres
    input = add_multiplication(input)
    print(input)
    if input == 'quit' or input == 'q' or input == 'exit':
        sys.exit()
    parsing(input)# try -> catch -> raise
