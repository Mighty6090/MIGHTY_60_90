h=int(input())
k=list(map(int,input().split()))
j=min(k)
p=[]
for i in range(0,len(k)):
    if k[i] not in p:
        p+=[k[i]]
        if k[i]==j:
            print(j,i+1)
