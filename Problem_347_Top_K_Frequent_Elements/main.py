"""
LeetCode Problem 347. Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Author: Matthew Holyk

Created: Nov 01, 2025
"""
a_list = [1,1,1,2,2,3]
b_list = [2]
c_list = [1,2,1,2,1,2,3,1,3,2]
# a tuple of tuples contain the menu options
menu_options = (('a', a_list),('b', b_list),
                ('c', c_list))

def prompt_user():
    print(f"Which input would you like assessed?")

    for t in menu_options:
        print(f"{t[0]:<4}: {t[1]}")

def top_k_frequent(nums: list[int], k: int) -> list[int]:
    """
        A function to identify the elements of the input list with the greatest population, "k" equals
        the amount of populations to identify.
        :param nums: a list of integers
        :param k: the amount of populations to identify
        :return: a list of "k" elements, the elements with the greatest population in the input list
        """
    count_dict = {} # the occurences of each value
    # a list of lists to hold elements of num, the frequency of the element if represented by it's index in frequency
    frequency = [[] for i in range(len(nums) + 1)]

    # for each element in nums increment the count(value) in count_dict
    for n in nums:
        count_dict[n] = 1 + count_dict.get(n, 0)
    # for each kvp in count_dict place the the value in the list at the index represented by the key
    for n, c in count_dict.items():
        frequency[c].append(n)

    # a list to hold the most populated elements
    output = []
    # iterate over frequency in reverse, reaching the most populated elements first
    for i in range(len(frequency)- 1, 0, -1):
        # add any elements encountered to the output list
        for n in frequency[i]:
            output.append(n)
            # end the function if the desired amount of elements has been reached
            if len(output) == k:
                return output

if __name__ == "__main__":
    entry = 1 # continually loop the menu until entry = 0

    while entry:
        input_collection = [] # a list to hold the input to be assessed
        prompt_user()         # display the options to the user
        # obtain input from the user
        chosen = input(f"Selection : ").strip()
        match chosen:
            case 'a':
                input_collection.extend(a_list)
            case 'b':
                input_collection.extend(b_list)
            case 'c':
                input_collection.extend(c_list)

        if len(input_collection):
            amount = int(input("How many of the most frequent elements would you like displayed? ").strip())
            # display the result to the user
            result = top_k_frequent(input_collection, amount)
            print(f"The {amount} most populated elements in the input are {result}.")