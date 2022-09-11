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
            print(unique)
            if s[lead] in unique:
                if len(unique) > curr_max:
                    curr_max = len(unique)
                unique = set()
                trail += 1
                lead = trail
            else:
                unique.add(s[lead])
                lead += 1
            print(unique)
        curr_max = max(curr_max, len(unique))
        return curr_max
