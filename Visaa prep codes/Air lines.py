X,N = map(int, input().split())
a = X*100
if a>=N:
    np = 0
else:
    b=N-a
    np=(b+99)//100
    
print(np)
