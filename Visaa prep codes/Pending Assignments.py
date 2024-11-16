X,Y, Z= map(int,input().split())
T = X*Y
A = Z*24*60
if T<=A:
    print("YES")
else:
    print("NO")
