lst=input("Enter the list of word separated by comma:")

a = lst.split(",")

def len_log(list1):

    max=len(list1[0])

    for i in list1:

        if len(i)>max:

            max=len(i)
            

    return  max

print("The length of longest word  is",len_log(a))
