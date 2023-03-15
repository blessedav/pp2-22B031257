import os
p = os.listdir(r"C:\Users\GIMISI\Desktop\pp2-labs\tsis 6\dirnfile")
for i in p:
    if os.path.isdir(i):
        print(i)
for i in p:
    if os.path.isdir(i) or os.path.isfile(i):
        print(i)
for i in p:
    if os.path.isfile(i):
        print(i)