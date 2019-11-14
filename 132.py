"""Write a program to sort the dictionary keys 
and values in alphabetical order using the values.
Input:
mydict ={2:56, 1:2, 5:12, 4:24, 6:18, 3:323}
Output:
[(1, 2), (5, 12), (6, 18), (4, 24), (2, 56), (3, 323)]
"""
mydict ={2:56, 1:2, 5:12, 4:24, 6:18, 3:323}
def sortkeys(d):
	x=sorted(d.items(),key=lambda x:x[1])
	return x

print(sortkeys(mydict))


