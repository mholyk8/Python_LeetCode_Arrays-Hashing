"""
LeetCode Problem 242. Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Author: Matthew Holyk

Created: Oct 25, 2025
"""

def isAnagram(s: str, t: str) -> bool:
    """
        A function to compare 2 strings and determine if they are anagrams of each other.
        :param s: a string
        :param t: a string
        :return: A bool representing whether the provided inputs were anagrams of each other.
        """
    if len(s) != len(t):
        return False

    dic_s, dic_t = {}, {}

    for i in range(len(s)):
        dic_s[s[i]] = 1 + dic_s.get(s[i], 0)
        dic_t[t[i]] = 1 + dic_t.get(t[i], 0)

    return dic_s == dic_t

if __name__ == '__main__':
    s = "anagram"   # default input
    t = "nagaram"   # default input

    # Obtain the strings to be compared from the user.
    s_input = input(f"Enter the first string you want to compare as an anagram[{s}]:").strip() or s
    t_input = input(f"Enter the string you want to compare to the first [{s_input}] as an anagram[{t}]:").strip() or t
    result = isAnagram(s_input, t_input)
    print(f"The result of the Anagram comparison of {s_input} & {t_input} is {result}.")