N,X,Y = map(int,input().split())
max = N*X
if 0 <= max and Y%X == 0:
    print("YES")
else:
    print("NO")
