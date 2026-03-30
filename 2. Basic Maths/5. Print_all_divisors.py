N=int(input())


# for i in range(1,N+1):
#     if N%i==0:
#         print(i,end=",")
#     else:
#         continue
a=[]
for i in range(1, int(N**0.5) + 1):
    if N % i == 0:
        a.append(i)
        if i != N // i:
            a.append(N // i)

print(sorted(a))