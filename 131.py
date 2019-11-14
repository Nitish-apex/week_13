"""Write a program to sort the values of first list using second list.
Input:
list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
list2 = [ 0,1,1,0,1,2,2,0,1]
Output: ['a', 'd', 'h', 'b', 'c', 'e', 'i', 'f', 'g']"""
list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
list2 = [ 0,1,1,0,1,2,2,0,1]
i=0
def sorter(x):
	global i
	i+=1
	return list2[i-1]
solis=sorted(list1,key=sorter)
print(solis)