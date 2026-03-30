N=int(input())
count=0
while N>0:
    # last_digit=N%10
    count+=1
    N//=10

print(count)


# TC = O(logN)
# SC = O(1)