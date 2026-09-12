n=int(input())
for o in range(n):
    h=int(input())
    f=list(map(int,input().split()))
    t=[]
    for i in range(0,h-1):
        for j in range(i+1,h):
            k=f[i]+f[j]+j-i
            t+=[k]
    t.sort()
    print(t[0])