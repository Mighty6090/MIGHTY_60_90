c=int(input())
f=0
for i in range(c):
    u,v,p=map(int,input().split())
    if u+v+p>=2:
        f+=1
print(f)