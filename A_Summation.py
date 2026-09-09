c=int(input())
a=list(map(int,input().split()))
g=0
for i in a:
    g+=i
if g<=0:
    print(g*(-1))
else:
    print(g)

    
    