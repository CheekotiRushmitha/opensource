def diff(N,m,arr):
    num1 = sum(x for x in arr if x%m!=0)
    num2 = sum(x for x in arr if x%m == 0)
    return num2-num1
N,m=map(int,input().split())
arr=list(map(int, input().split()))
if len(arr) != N:
    print("Invalid")
else:
    print(diff(N,m,arr))
