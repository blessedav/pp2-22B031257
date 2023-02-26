def mygenerator(n):
    for i in range(n):
        yield i*i

n = int(input())
for val in mygenerator(n):
    print(val)