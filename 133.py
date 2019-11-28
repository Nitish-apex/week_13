""" Write a program to remove all duplicate words from a given sentence """
str = input("enter a sentence")
str = str.split(" ")
str = set( str )
print ( *str )


