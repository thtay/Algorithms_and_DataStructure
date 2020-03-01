from linkedlist import Node,UnorderedList
import unittest

def kth(k,l1):
	"""
	Return the Kth to last element in a singly linked list
	1>2>3>5>5>7>9
	0 1 2 3 4 5 6
	k = 1
	return the 5
	"""
	first = l1.head
	second = l1.head
	n = 0
	i = 0
	ans = 0
	found = False
	while first != None:
		n += 1
		first = first.next
	n = n -1
	while second != None and not found:
		if i == (n-k):
			ans = second.data
		i += 1
		second = second.next
	return ans

def kth2(k,l1):
	"""
	Return the Kth to last element in a singly linked list
	1>2>3>5>5>7>9
	0 1 2 3 4 5 6
	k = 1
	return the 5
	"""
	lead = l1.head
	follow = l1.head

	for i in range(k+1):
		if lead == None:
			return 'out of bounds'
		lead = lead.next

	while lead != None:
		lead = lead.next
		follow = follow.next
	return follow.data



		
# l1 = UnorderedList()
# l2 = UnorderedList()
# l2.addFromList([1,2,3,44,5,5,6])
# l2.display()
# print()
# l1.add(1)
# l1.add(2)
# l1.add(3)
# l1.add(4)
# l1.add(5)
# l1.add(6)
# l1.add(7)
# l1.add(8)
# l1.display()
# #l1.remove_duplicate()
# print()
# print(kth(3,l1))
# print(kth2(3,l1))