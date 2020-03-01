'''
String compression:  Implement a method to perform basic string compression using the
counts of repeated characters. For example, the string aabcccccaa would be a2b1c5a3.
If the "compressed" string would not become smaller than the orignal string, your
method should return the original string. You can assume the string has only uppercase
and lowercase letters (a-z).
'''

'''
let's iterate through the word: two pointer appraoch would work here
aaabbbcccaakk
^^
if

if i and f are the same increment only f and count another

aaabbbcccaakk
^ ^
i f

same as above

aaabbbcccaakk
^  ^
i  f

not the same. so append i and the counter and move i to f and increment f by 1

'''

def stringComp(word):
	ans = ""
	forward = 1
	i = 0
	counter = 1

	while forward < len(word):
		if word[i] == word[forward]:
			counter += 1
			forward += 1
		else:
			ans += word[i]
			ans += str(counter)
			i = forward
			forward += 1
			counter = 1

		if forward + 1 > len(word):
			ans += word[i]
			ans += str(counter)

	if len(ans) >= len(word):
		return word
	return ans

'''
Test Cases
'''

print(stringComp('aaabbbcccaakk'))
print(stringComp('aabbbcccaakkc'))
print(stringComp('abcnfjdk'))
print(stringComp('aabbbcccaakkc'))
print(stringComp('aabbbcccaaaakkcb'))