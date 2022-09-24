# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.



def lengthOfLongestSubstring(s):
        lead=0
        trail=0
        length = len(s)
        unique = set()
        curr_max = 0
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        while lead < length:
            # print(unique)
            if s[lead] in unique:
                if len(unique) > curr_max:
                    curr_max = len(unique)
                unique = set()
                trail += 1
                lead = trail
            else:
                unique.add(s[lead])
                lead += 1
            # print(unique)
        curr_max = max(curr_max, len(unique))
        return curr_max


# Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.

# Example 1:

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
# Example 2:

# Input: target = 4, nums = [1,4,4]
# Output: 1
# Example 3:

# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0


# Constraints:

# 1 <= target <= 109
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 104


# Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).

def minSubArrayLen(target, nums):
    """minSubArrayLen

    :param target: The target sum
    :type target: int
    :param nums: The list of nums to use
    :type nums: list
    """
    # lead = 0
    # trail = 0
    # min_len = 0
    # current_sum = 0

    # if len(nums) == 0:
    #     return 0
    # if len(nums) == 1:
    #     return 1

    # while lead < target:
    #     current_sum += nums[lead]
    #     if current_sum > target:
    #         return min_len
    #     else:


