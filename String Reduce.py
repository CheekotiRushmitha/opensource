p=input()
r = ""
count = 1
for i in range(1,len(p)):
    if p[i] == p[i - 1]:
        count+=1
    else:
        r+= p[i-1]+str(count)
        count = 1
r+=p[-1]+str(count)
print(r)
        
