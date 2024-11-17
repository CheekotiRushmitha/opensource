def rev(n):
    is_neg = n<0
    reverse = int(str(abs(n))[::-1])
    if reverse>(2**31-1):
        print(0)
        return
    if is_neg:
        reverse = -reverse
    print(reverse)
n = int(input())
rev(n)
