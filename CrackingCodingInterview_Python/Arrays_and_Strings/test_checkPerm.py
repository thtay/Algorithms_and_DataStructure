import unittest
from checkPerm import checkPerm,checkPerm2

class TestCheckPerm(unittest.TestCase):
	"""
	Testiing the checkPerm and checkPerm2 functions
	run all unit test in directory with: python3 -m unittest
	"""
	def test_checkPerm(self):
		self.assertEqual(checkPerm('hi','hello'), False)
		self.assertEqual(checkPerm('god','dog'), True)

		