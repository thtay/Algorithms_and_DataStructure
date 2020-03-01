"""
 Is Unique: Implement an alogrithm to determin if a string
 has all unqiue characters. What if you cannot use
 additional data structures?
"""

def isUnique(word):
	from collections import Counter

	count = Counter(word)

	for i in count.values():
		if i > 1:
			return False

	return True

def isUnique2(word):
	##Use a hash map to check if there will be a repeat
	check = set()

	for letter in word:
		if letter not in check:
			check.add(letter)
		else:
			return False
	return True

"""
Test Cases
"""

print(isUnique('cat'))
print(isUnique('hat'))
print(isUnique('hello'))
print(isUnique('lkdklj23lkjdkfjd'))
print('\n')

print(isUnique2('hat'))
print(isUnique2('cat'))
print(isUnique2('hello'))
print(isUnique2('lkdklj23lkjdkfjd'))