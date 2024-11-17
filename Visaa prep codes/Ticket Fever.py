t=int(input())
a=[]
for i in range(t):
    n,m=map(int, input().split())
    b=max(0,n-m)
    a.append(b)
    
for res in a:
    print(res)
