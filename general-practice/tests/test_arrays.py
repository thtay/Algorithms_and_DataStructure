import imp
from multiprocessing.spawn import import_main_path
import unittest
from unittest import TestCase
# from general_practice import lengthOfLongestSubstring
import general_practice.arrays as arr

class arraysTest(unittest.TestCase):

    def test_arrays(self):
        """
        Case: pwwkey
        Expected: 3
        """
        test_string = 'pwwkey'
        ans = arr.lengthOfLongestSubstring(test_string)
        self.assertEquals(ans, 3)

