T = int(input())
a=[]
for i in range(T):
    x,y=map(int, input().split())
    b=max(0,x-y+1)
    a.append(b)
for res in a:
    print(res)
