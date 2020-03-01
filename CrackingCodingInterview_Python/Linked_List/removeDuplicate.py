'''
Remove Dupilctes: Write code to remove dupilates from an unsorted
linked list.

Follow up how would we solve this without a temp buffer.
'''

'''
Checking for duplicate from a linked list: We need to iterate
through the list at least once. And also need another array to
keep track of the unique values so far.
'''

from linkedlist import Node,UnorderedList
		
def remove_duplicate(l1):
    current = l1.head
    unique = set()
    prev = None
    while current != None:
        if current.data in unique:
            #remove
            prev.next = current.next
        else:
            unique.add(current.data)
            prev = current
        current = current.next
        


# l1 = UnorderedList()
# l1.add(1)
# l1.add(1)
# l1.add(1)
# l1.add(2)
# l1.display()
# #l1.remove_duplicate()
# remove_duplicate(l1)
# print()
# l1.display()
# print()
# l2 = UnorderedList()
# l2.addFromList([1,1,1,2])
# l2.display()
# remove_duplicate(l2)
# print()
# l2.display()

