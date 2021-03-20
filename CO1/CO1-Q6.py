lst=['anu','ammu','ananya']
print(lst)
i=0
count=0
while i<len(lst):
	count=count+lst[i].count('a')
	i=i+1


	
print("Count of a is: " ,count)
