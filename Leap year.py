def year(n):
    if (n%4==0 and n%100!=0) or (n%400==0):
        return True
    else:
        return False
n=int(input())
if year(n):
    print("YES")
else:
    print("NO")
