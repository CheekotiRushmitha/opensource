X,Y,Z=map(int,input().split())
max=Z-Y
if max<=0:
    print(0)
else:
    max_mangoes = max // X
    print(max_mangoes)
