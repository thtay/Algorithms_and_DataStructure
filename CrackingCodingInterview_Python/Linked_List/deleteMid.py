from linkedlist import Node,UnorderedList

def delete_mid(n):
	"""
	Delete Middle Node: Implementing an alogirthm to delete a node 
	in the middle (i.e., any node but the first and last node, not
	necessrily the exact middle) of a singly linked list, given only
	access to that node.
	Example
	Input: the node c from the linked list a->b->c->d->e->f
	Result: nothing is returned, but the new list which looks like
	a->b->d->e->f
	"""

	#Given a node, let's assume the node has a prev and next element
	#We want to delete this node, normall we should set the prev to the
	#next node, skipping over the current node: prev->cur->next 
	# prev-> next.
	#But here we do not have the prev node, only the current node
	#and all upcoming nodes: cur->next->nextnext. The way to delete
	#the current node would be copy the next node to the cur and
	#point to the nextnext: copyofnext->nextnext

	n.data = n.next.data
	n.next = n.next.next