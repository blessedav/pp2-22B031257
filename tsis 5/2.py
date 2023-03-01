import re
txt = input()
x = re.search('a.{1}b', txt)
y = re.search('a.{2}b', txt)
if re.search('a.{1}b', txt):
    print(x)
elif re.search('a.{2}b', txt):
    print(y)
else:
    print("Error")