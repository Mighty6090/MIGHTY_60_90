c=int(input())
t=list(map(int,input().split()))
f=int(input())
l=[]
for i in range(0,len(t)):
    if t[i] not in l:
        if t[i]==f:
            l+=[i]
if l==[]:
    print("-1")
else:
    print(l[0])
        
        
            
        



