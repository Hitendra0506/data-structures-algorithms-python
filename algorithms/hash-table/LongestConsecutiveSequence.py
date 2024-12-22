'''
Set: Longest Consecutive Sequence ( ** Interview Question)
Given an unsorted array of integers, write a function that finds the length of the  longest_consecutive_sequence (i.e., sequence of integers in which each element is one greater than the previous element).

Use sets to optimize the runtime of your solution.

Input: An unsorted array of integers, nums.

Output: An integer representing the length of the longest consecutive sequence in nums.

Example:



Input: nums = [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive sequence in the input array is [4, 3, 2, 1], and its length is 4.
'''

def longest_consecutive_sequence(nums):
    
    num_set = set(nums)
    max_len = 0

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_len = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_len += 1

            max_len = max(max_len, current_len)

    return max_len

'''
# The below code does not work for unordered sequences liks [1,2,0,1]

def longest_consecutive_sequence(nums):
    hm = {}
    max_len = 0
    for n in nums:
        if (n in hm):
            continue
        hm[n] = 0
        if (n-1 in hm):
            hm[n] += hm[n-1]
        if (n+1 in hm):
            hm[n] += hm[n+1]
        hm[n] += 1
        max_len = max(max_len,hm[n])
    return max_len
'''