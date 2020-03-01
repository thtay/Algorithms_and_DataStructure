import unittest
from removeDuplicate import remove_duplicate
from linkedlist import Node, UnorderedList

class Testkth(unittest.TestCase):
	"""
	Testig the remove_duplicate function
	run all unit test in directory with: python3 -m unittest
	"""
	def test_kth(self):
		#Test that all duplicated are removed, valid inputs
		l1 = UnorderedList()
		l1.addFromList([1,1,1,1,1])
		remove_duplicate(l1)
		self.assertEqual(l1.linkedToList(),[1])

		l1.addFromList([1,2,3,3,4,45,6,4,7])
		remove_duplicate(l1)
		self.assertEqual(l1.linkedToList(),[1,2,3,4,45,6,7])

 