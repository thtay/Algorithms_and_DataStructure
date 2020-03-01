"""
Palidrome Permutation: Given a string, write a functin to check if
it is a permuation of a palidrome. A palidrome is a word or phrase
that is the same forwards and backwards. A permuation is a 
reaggragnment of letters. The palindrome does not need to be 
limited to just a dictionary words.
"""

def permPali(word):

	## modify the string to only consit of letters not even spaces
	onlyletters = ""
	for letter in word:
		letter = letter.lower()
		if ord(letter) >= 97 and ord(letter) <= 122:
			onlyletters += letter

	from collections import Counter

	wordCount = Counter(onlyletters)
	oneOdd = False

	for c in wordCount.values():

		if c%2 != 0:
			##Not an even number
			if oneOdd:
				return False
			oneOdd = True
	return True


"""
Test Cases
"""

print(permPali('Tact Coa'))