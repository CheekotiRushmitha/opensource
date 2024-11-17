T = int(input())
a=[]
for i in range(T):
    X = int(input())
    if 67<= X <= 45000:
        a.append("YES")
    else:
        a.append("NO")
for res in a:
    print(res)
