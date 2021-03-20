rows = int(input("Enter the number of rows: "))  
   
for i in range(0, rows):   
    for j in range(0, i + 1):  
        print("*", end=' ')   
    print(" ")  
# For second pattern  
for i in range(rows , 0, -1):  
    for j in range(0, i - 1):  
        print("*", end=' ')  
    print(" ")  
