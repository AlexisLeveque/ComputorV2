import sys
import re

while 1:
    input = raw_input('> ')
    input = re.sub('[ \t]', '', input)

    if input == 'quit' or input == 'q' or input =='exit':
        sys.exit()