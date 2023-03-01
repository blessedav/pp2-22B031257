import re
txt = 'wgeerger_egregerignerio'
x = re.findall("[a-z]+\_+[a-z]", txt)
if x:
    print(x)
else:
    print("No match")