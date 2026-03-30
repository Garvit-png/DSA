N=int(input())
count=len(str(N))
temp=N
value=0
while N>0:
    d=N%10
    value+=d**count
    N//=10

if (temp==value):
    print(True)
else:
    print(False)
