try:
    n = int(input("Enter the number:"))
    if(n%2!=0):
        raise Exception("Error! number is not even")
    else:
        print("Even")
except Exception as e:
    print("Raising an Exception",e)