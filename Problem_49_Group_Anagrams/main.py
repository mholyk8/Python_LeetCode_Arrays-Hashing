"""
Given an array of strings strs, group the together. You can return the answer in any order.

Author: Matthew Holyk

Created: Oct 31, 2025
"""
from collections import defaultdict

# a tuple of tuples contain the menu options
menu_options = (('a', '["eat","tea","tan","ate","nat","bat"]'),('b', '[""]'),
                ('c', '["a"]'),('x', 'Exit'))

def prompt_user():
    print(f"Which input would you like assessed?")

    for t in menu_options:
        print(f"{t[0]:<4}: {t[1]}")

def group_anagrams(strs: list[str]) -> list[list[str]]:
    # map keys to lists of anagrams
    grouped = defaultdict(list)

    for s in strs:
        # a list of 26 zeroes to count the number of each letter in the assessed string
        letter_list = [0] * 26

        # for each letter in the current string being assessed, increment the count in
        # letter_list, corresponding to that letter's position in the alphabet
        for l in s:
            letter_list[ord(l)-ord("a")] += 1

        # cast letter_list to a tuple as lists are not allowed to be dictionary keys
        grouped[tuple(letter_list)].append(s)

    return list(grouped.values())

if __name__ == "__main__":
    entry = 1 # continually loop the menu until entry = 0
    input_a = ["eat","tea","tan","ate","nat","bat"]
    input_b = [""]
    input_c = ["a"]

    while entry:
        prompt_user()
        chosen = input("Selection : ").strip()

        match chosen:
            case 'a':
                anagrams = group_anagrams(input_a)
                print(anagrams)
            case 'b':
                anagrams = group_anagrams(input_b)
                print(anagrams)
            case 'c':
                anagrams = group_anagrams(input_c)
                print(anagrams)
            case 'x':
                # end the program if the user enters no choice
                entry = 0
            case _: # default case
                # print the list again if the user enters an invalid choice
                prompt_user()