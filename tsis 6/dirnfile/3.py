import os
p = os.listdir(r"C:\Users\GIMISI\Desktop\pp2-labs\tsis 6\dirnfile")

if os.path.exists(p):
    print("file and dir portions of the path")
    print(os.path.basename(p))
    print(os.path.dirname(p))
else:
    print("pass doesnt exist!")