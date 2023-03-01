import re
txt = 'hello_world'
txt2 = txt.upper()
camel = ''
i = 0
while(i != len(txt)):
    if txt[i] == '_':
        camel += txt[i] + txt2[i+1]
        i += 2
    else:
        camel += txt[i]
        i += 1
camel = re.sub('_', '', camel)
print(camel)
