N=int(input("ENTER A NUMBER:"))
print("The factors of {} are,".format(N))
for i in range(1,N+1):
    if N % i == 0:
        print(i)
