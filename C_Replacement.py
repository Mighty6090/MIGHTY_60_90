n=int(input())
l=list(map(int,input().split()))
h=[]
for i in l:
    if i<0:
        h+=[2]
    elif i>0:
        h+=[1]
    else:
        h+=[0]
for i in h:
    print(i,end=" ")
