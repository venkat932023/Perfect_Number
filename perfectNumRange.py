def perfect(n):
    s = 0
    for i in range(1,(n//2)+1):
        if n%i == 0:
            s = s+i
    if s == n:
        return 1
    else:
        return 0

n = int(input())
for i in range(1,n+1):
    if perfect(i) == 1:
        print(i,end=" ")