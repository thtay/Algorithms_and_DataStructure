import unittest
from kthelement import kth,kth2
from linkedlist import Node, UnorderedList

class Testkth(unittest.TestCase):
	"""
	Testig the kth and kth2 function
	run all unit test in directory with: python3 -m unittest
	"""
	def test_kth(self):
		#Test the kth value is removed, with valid inputs
		l1 = UnorderedList()
		l1.addFromList([1,2,3,4,5,6,7])
		self.assertEqual(kth(0,l1),7)
		self.assertEqual(kth(1,l1),6)
		self.assertEqual(kth(6,l1),1)
		self.assertEqual(kth2(0,l1),7)
		self.assertEqual(kth2(1,l1),6)
		self.assertEqual(kth2(6,l1),1)
