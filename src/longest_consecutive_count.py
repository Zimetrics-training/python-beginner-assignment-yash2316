"""
Problem: Find the Longest Consecutive Sequence
Given an unsorted array of integers, write a function longest_consecutive(nums) 
that returns the length of the longest consecutive elements sequence.

Example: if nums = [100, 4, 200, 1, 3, 2]; The function should return 4, 
since the longest consecutive elements sequence is [1, 2, 3, 4].

Look for difference of 1 between two consecutive numbers.
"""
def longest_consecutive(nums):
    # Implement your method here
    sorted_list = sorted(nums)

    cur_len = 1
    longest_streak = 0

    for i in range(1, len(sorted_list)):
        if sorted_list[i-1] + 1 == sorted_list[i]:
            cur_len += 1
        else:
            cur_len = 1
        
        if cur_len > longest_streak:
            longest_streak = cur_len

    return longest_streak
