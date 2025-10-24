"""
LeetCode Problem 217. Contains Duplicate
Given an integer array nums, RETURN TRUE if any value
appears at least twice in the array, and RETURN FALSE
if every element is distinct.

Author: Matthew Holyk

Created: Oct 24, 2025
"""

def contains_duplicate(num_list: list[int]) -> bool:
    uniques = set()     # Create a hashset to compare the existence of List elements to
                        # as hashsets don't allow duplicates to exist.

    for n in num_list:
        # If a duplicate is found, end the search and return True.
        if n in uniques:
            return True

        # Add the list element to the hashset. If it is a duplicate the contents of the
        # set will not change due to the rules of hashsets.
        uniques.add(n)
    # If this point is reached, no duplicates were found, return False.
    return False

if __name__ == '__main__':
    """
    Python does not have arrays, so I will use a List.
    """
    nums = [1, 2, 3, 1]               # Output: True
    # nums = [1,2,3,4]                # Output: False
    # nums = [1,1,1,3,3,4,3,2,4,2]    # Output: True

    # Supply the input to the function to determine if duplicates are contained in the collection.
    duplicates_found = contains_duplicate(nums)

    # Display the results to the console.
    print(f"The result of the search for duplicates in {nums} is {duplicates_found}.")