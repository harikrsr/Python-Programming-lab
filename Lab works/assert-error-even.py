def predict(a):
    b=a%2
    assert(b==0)
    return b
even=int(input("enter a number:"))
print(predict(even))