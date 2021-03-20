li=[33,88,9,12,45,78,11,77]
print("ORIGINAL LIST:",li)
for i in li:
    if (i % 2 ==0):
        li.remove(i)
        
    
print("List after removing even numbers:",li)
