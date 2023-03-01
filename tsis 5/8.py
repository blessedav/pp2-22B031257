import re
txt = 'HelloWorld'
x = re.findall('[A-Z][^A-Z]*', txt)
print(x)