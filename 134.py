"""
Given an integer ‘n’, write a Python function that returns
true if binary representation of x is
palindrome else return false.
Examples:
Input : n = 9
Output : True
Binary representation of n=9 is 1001 which is palindrome as well.
Input : n = 10
Output : False
Binary representation of n=10 is 1010 which is not palindrome.
"""
x=int(input("enter a number: "))
y=bin(x)
z=y[2:]
if z==z[::-1]:
	print("palindrome")
else:
	print("not a palindrome")