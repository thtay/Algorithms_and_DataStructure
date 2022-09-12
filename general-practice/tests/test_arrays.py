import imp
from multiprocessing.spawn import import_main_path
import unittest
from unittest import TestCase
# from general_practice import lengthOfLongestSubstring
import general_practice.arrays as arr

class arraysTest(unittest.TestCase):

    def test_arrays_length_of_longest_subString(self):
        """
        Case: pwwkey
        Expected: 3
        """
        test_string = 'pwwkey'
        ans = arr.lengthOfLongestSubstring(test_string)
        self.assertEquals(ans, 3)

    def test_minSubArrayLen(self):
        """
        minSubArrayLen Tests
        """
        test_array_1 = [2,3,1,2,4,3]
        test_array_1_target = 7
        test_array_1_ans = 2
        test_array_2 = [1,4,4]
        test_array_2_target = 4
        test_array_2_ans = 1
        test_array_3 = [1,1,1,1,1,1,1,1]
        test_array_3_target = 11
        test_array_3_ans = 0

        self.assertEquals(arr.minSubArrayLen(test_array_1_target,test_array_1), test_array_1_ans)
        self.assertEquals(arr.minSubArrayLen(test_array_2_target,test_array_2), test_array_2_ans)
        self.assertEquals(arr.minSubArrayLen(test_array_3_target,test_array_3), test_array_3_ans)