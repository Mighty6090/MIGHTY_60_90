n=int(input())
f=list(map(int,input().split()))
for j in range(n):
    for i in range(0,n-j-1):
        if f[i]>f[i+1]:
            f[i],f[i+1]=f[i+1],f[i]
for i in f:
    print(i,end=" ")


    
