"""
One Away: There are three types of edits that can be performed on a string: insert a 
character, remove a character, or replace a character. Given two strings, write a 
function to check if they are one edit (or zero edit) away.
"""

"""
Notes:

So we just need to check if the two strings are only one (edit,replace,add) away from 
each other.

Let's look at Add:
if we need to add one letter. Then the lengths must be 1 away from each other.

Let's look at replace:
If we only need to replace, the lengths of the two strings are equal. So only we only
need to check if there is only one item in the string that is not the same in order.

Lets look at Remove:
Similar to add, we are short by 1 character. But this time we are removing one

The order of the string matter.

"""

def oneAway(word1,word2):
	if word1 == word2:
		return True

	if len(word1) == len(word2):
		##Should only need to replace one letter
		oneAway = False
		for i in range(len(word1)):
			if word1[i] != word2[i]:
				if oneAway:
					return False	
				oneAway = True

		return True	
	elif abs(len(word1)-len(word2)) > 1:
		return False
	else:
		##let's say we need to add
		'''
		word1 = hello
		word2 = hllo
		let's loop through the shorter string first:
			word 1 = h
			word 2 = h 

			word 1 = e
			word 2 = l not 
			*** keep the position for word2 do not increment

			.....
			should be good
		'''
		## lets say we need to remove
		'''
		word1 = hello
		word2 = heollo
		let's loop through the shorter string:
			word 1 = h
			word 2 = h

			word 1 = e
			word 2 = e

			word 1 = l
			word 2 = o
			*** keep the position for word1 do not increment
			**
		'''
		##Need to add/remove one character
		if len(word1) > len(word2):
			larger = word1
			smaller = word2
		else:
			larger = word2
			smaller = word1

		oneAway = False

		l = s = 0

		while l < len(larger) and s < len(smaller):
			if smaller[s] != larger[l]:
				if oneAway:
					return False
				oneAway = True
				l += 1
			else:
				l += 1
				s += 1
		return True


'''
Test Cases
'''

print(oneAway('hello','hell'))
print(oneAway('hello','hellooo'))
print(oneAway('cat','kitten'))
print(oneAway('cat','cat'))