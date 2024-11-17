def find_pair():
    N=int(input())
    arr=list(map(int,input().split()))
    K=int(input())
    a=set()
    for num in arr:
        if K-num in a:
            print("true")
            return
        a.add(num)
    print("false")
find_pair()
