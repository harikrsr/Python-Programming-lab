n=int(input("ENTER THE LIMIT:"))
f=0                                         
s=1
if n<=0:
    print("The requested series is",f)
else:
    print(f,s,end=" ")
    for x in range(2,n):
        next=f+s                           
        print(next,end=" ")
        f=s
        s=next
