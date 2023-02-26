def gener(n):
    for i in range(n):
        if i == 0:
            continue
        if i % 2 == 0:
            yield i
n = int(input())
mylist = []
for val in gener(n):
    mylist.append(str(val))

print(', '.join(mylist))