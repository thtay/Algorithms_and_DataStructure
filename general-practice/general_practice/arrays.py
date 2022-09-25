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
        start = 0
        end = 0
        length = len(s)
        unq = dict()
        count = 0
        # Initialize the dictionary to have a letter for each letter in s with count of 0
        for letter in s:
            unq[letter] = 0

        while end < length:
            unq[s[end]] += 1
            while unq[s[end]] > 1:
                unq[s[end]] -= 1
                start += 1
            count = max(count, end-start+1)
            end += 1
        return count
        # lead=0
        # trail=0
        # length = len(s)
        # unique = set()
        # curr_max = 0
        # if len(s) == 0:
        #     return 0
        # if len(s) == 1:
        #     return 1
        # while lead < length:
        #     # print(unique)
        #     if s[lead] in unique:
        #         if len(unique) > curr_max:
        #             curr_max = len(unique)
        #         unique = set()
        #         trail += 1
        #         lead = trail
        #     else:
        #         unique.add(s[lead])
        #         lead += 1
        #     # print(unique)
        # curr_max = max(curr_max, len(unique))
        # return curr_max
# class Solution {
# public:
#     int lengthOfLongestSubstring(string s) {

#         //SLIDING WINDOW  - TIME COMPLEXITY O(2n)
#         //                  SPACE COMPLEXITY O(m)   //size of array

#         int store[256]={0}; //array to store the occurences of all the characters
#         int l=0;    //left pointer
#         int r=0;    //right pointer
#         int ans=0;  //initializing the required length as 0

#         while(r<s.length())     //iterate over the string till the right pointer reaches the end of the string
#         {
#             store[s[r]]++;      //increment the count of the character present in the right pointer

#             while(store[s[r]]>1)    //if the occurence become more than 1 means the char is repeated
#             {
#                 store[s[l]]--;   //reduce the occurence of temp as it might be present ahead also in the string
#                 l++;         //contraction of the present window till the occurence of the 't' char becomes 1
#             }

#             ans = max(ans,r-l+1);    //As the index starts from 0 , ans will be (right pointer-left pointer + 1)
#             r++;        // now will increment the right pointer
#         }
#         return ans;
#     }
# };

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


