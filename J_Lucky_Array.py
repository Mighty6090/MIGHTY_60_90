n=int(input())
f=list(map(int,input().split()))
f.sort()
g=f[0]
h=0
for i in f:
    if g==i:
        h+=1
if h%2==0:
    print("Unlucky")
else:
    print("Lucky")

