N=int(input())
a=[]
for i in range(N):
    b=list(map(int, input().split()))
    a.append(b)
mirror = [b[::-1] for b in a]
for b in mirror:
    print(' '.join(map(str, b)))
