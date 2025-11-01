"""
LeetCode Problem 1. Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add
up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Author: Matthew Holyk

Created: Oct 27, 2025
"""

def two_sum(nums: list[int], target: int) -> list[int]:
    diff_dict = {} # a dictionary keyed by elements of the input

    for i, n in enumerate(nums):
        difference = target - n     # determine what must be added to n to match the target
        if difference in diff_dict:
            return [diff_dict[difference], i]
        diff_dict[n] = i

if __name__ == '__main__' :
    # nums_list = [2,7,11,15]  # Output: [0,1]
    # target_input = 9
    nums_list = [3,2,4]    # Output: [1,2]
    target_input = 6
    # nums_list = [3,3]      # Output: [0,1]
    # target_input = 6

    user_target = int(input(f"What sum would you like searched in the collection {nums_list}? ").strip()) or target_input
    indices = two_sum(nums_list, user_target)
    print(f"The indices {indices} hold the elements that add up to the target [{user_target}].")