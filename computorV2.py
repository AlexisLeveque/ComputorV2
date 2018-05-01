# -*- coding: utf-8 -*-
import sys
import re
from resolve import parsing


while 1:
    input = raw_input('> ')
    input = re.sub(r'[ \t]', '', input).lower()
    print(input)
    if input == 'quit' or input == 'q' or input == 'exit':
        sys.exit()
    parsing(input)
