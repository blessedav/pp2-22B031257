import os
p=(r"C:\Users\GIMISI\Desktop\pp2-labs\tsis 6\dirnfile\filewillbedeleted.txt")
if os.path.exists(p):
    os.remove(p)
else:
    print("this file doesnt exist")