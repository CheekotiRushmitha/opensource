a=input().strip()
vig,charan=a.split()
if(vig == 'R' and charan == 'P'):
    print("Charan")
elif(vig == 'P' and charan == 'R'):
    print("Vignesh")
elif(vig == 'P' and charan == 'S'):
    print("Charan")
elif(vig == 'S' and charan == 'P'):
    print("Vignesh")
elif(vig == 'S' and charan == 'R'):
    print("Charan")
elif(vig == 'R' and charan == 'S'):
    print("Vignesh")
else:
    print("NULL")
