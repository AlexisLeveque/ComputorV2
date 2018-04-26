import re


function_regex = re.compile('^[a-z]+\(')
text = 'sdjifn + retuio('
index = 9
if re.match(r'^[a-z]+\(', text[index:],):
    print('yea')
    print(text)