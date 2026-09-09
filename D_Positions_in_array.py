h=int(input())
f=list(map(int,input().split()))
for i in range(0,len(f)):
    if f[i]<=10:
        print("A["+str(i)+"] =",f[i])