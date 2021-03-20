n1=int(input("ENTER FIRST NUM:"))
n2=int(input("ENTER SECOND NUM:"))
gcd=1
if n1%n2==0:
    print(n2)
for k in range(int(n2 / 2), 0, -1):
        if n1 % k == 0 and n2 % k == 0:
            gcd = k
            break
print(k)

