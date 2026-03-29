n = int(input())

for i in range(1, n + 1):
    start = i % 2
    for j in range(i):
        print(start, end="")
        start = 1 - start
    print()