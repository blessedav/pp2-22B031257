def gener(n):
    for i in range(n):
        if i == 0:
            continue
        if i % 3 == 0:
            if i % 4 == 0:
                yield i
n = int(input())
for val in gener(n):
    print(val)
