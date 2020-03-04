from linkedlist import Node,UnorderedList

def sumList(l1,l2):
	"""
	Sum Lists: You have two numbers represented by a linked 
	list, where each node contains a single digit. The digits
	are stored in reverse order, such that the 1st digit is
	at the head of the list. Write a function that adds the
	two numbers and returns the sum as a linked list.
	Example:
	Input: (7->1->6) + (5->9->2). That is 617 + 295
	Ouptut: 2->1->9. That is 912
	Follow up
	Suppose the digits are stored in a forward order. Repeat
	the above problem.
	Input: (6->1->7) + (2->9->5). That is 617 + 295
	Output: 9->1->2. That is 912.
	"""

	#First Case:
	#Since the number is already in reversed order, we can
	#just add each values togeter like you would do when
	#manually adding two numbers. Like so,
	# 7->1->6
	#+5->9->2
	#We do the following:
	#1. Add 7+5, getting 12. it is above 9 so result is 12-10 =2,
	#with carry over of 1
	#2. Add 1+9 +1 carry over from before, getting 11, again is
	#above 9 so 11-10 = 1, with carry over of 1 again
	#3. Add 6+2 +1 from carry over, getting 9 it is not above 9, so
	#no carry over in this case.

	dum = current =  UnorderedList()
	remainder = 0
	l1 = l1.head
	l2 = l2.head

	while l1 != None and l2 != None:
		temp = l1.data + l2.data + remainder
		if temp > 9:
			current.add(temp-10)
			carryover = 1
		else:
			current.add(temp)
			carryover = 0
		l1 = l1.next
		l2 = l2.next


	while l1 != None:
		temp = l1.data + remainder
		if temp > 9:
			current.add(temp-10)
			carryover = 1
		else:
			current.add(temp)
			carryover = 0
		l1 = l1.next

	while l2 != None:
		temp = l2.data + remainder
		if temp > 9:
			current.add(temp-10)
			carryover = 1
		else:
			current.add(temp)
			carryover = 0
		l2 = l2.next

	if carryover != 0:
		current.add(1)

	return dum


# p1 = UnorderedList()
# p1.addFromList([1,2,3])
# p1.display()
# print()
# p2 = UnorderedList()
# p2.addFromList([1,2,3])
# p3 = sumList(p1,p2)
# p2.display()
# print()
# p3.display()
