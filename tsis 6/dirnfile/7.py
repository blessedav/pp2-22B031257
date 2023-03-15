f1=open("copy.txt", "r")
f2=open("copytohere.txt", "w")
for line in f1:
    f2.write(line)