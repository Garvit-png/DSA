#Extre Brute Force

N=int(input())

count=0
# for i in range(1,N+1):
#     if N%i==0:
#         count+=1
    
# if count==2:
#     print("yes,it is a prime number")
# else:print("It is not a prime number")


for i in range(1,int(N**0.5)+1):
    if (N%i==0):
        count+=1
        if i!=(N//i):
            count+=1
if count==2:
    print("YES")
else:print("NO")


