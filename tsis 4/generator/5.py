def gener(n):
    for i in range(n, -1, -1):
        yield i

n = int(input())
for val in gener(n):
    print(val)