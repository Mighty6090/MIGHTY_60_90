h=int(input())
f=list(map(int,input().split()))
g=f[::-1]
if f==g:
    print("YES")
else:
    print("NO")