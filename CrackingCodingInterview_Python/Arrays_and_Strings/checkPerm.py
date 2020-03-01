"""
Check permutatin: Given two strings, write a method to decide if one is
permutatin of the other.
"""

## Just sort the two words.
def checkPerm(word1, word2):
	return sorted(word1) == sorted(word2)


## Count the number of time a word occur
def checkPerm2(word1, word2):
	from collections import Counter

	return Counter(word1) == Counter(word2)

"""
Test Cases
"""

# print(checkPerm('hi','hello'))
# print(checkPerm('dog','god'))

# print(checkPerm2('hi','hello'))
# print(checkPerm2('dog','god'))