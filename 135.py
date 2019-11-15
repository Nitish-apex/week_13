"""
5. Given a dictionary and a character array, print all valid words that are possible using
characters from the array.
Note: Repetitions of characters is not allowed.
Examples:
Input : Dict = ["go","bat","me","eat","goal","boy", "run"]
arr = ['e','o','b', 'a','m','g', 'l']
Output : go, me, goal.
"""
Dict = ["go","bat","me","eat","goal","boy", "run"]
arr = ['e','o','b', 'a','m','g', 'l']
for x in Dict:
	bool=True
	for i in x:
		if i not in arr:
			bool=False
		if x.count(i)>arr.count(i):
			bool=False
	if bool:print(x)

