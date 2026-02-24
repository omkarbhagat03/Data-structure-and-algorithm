"""
LeetCode #9 – Palindrome Number

Problem Statement:
Given an integer x, return True if x is a palindrome,
and False otherwise.

A palindrome number reads the same forward and backward.

Example:
Input: 121
Output: True

Input: -121
Output: False

Time Complexity: O(log10 n)
    - We process only half of the digits of the number.

Space Complexity: O(1)
    - No extra data structures are used.
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Approach:
        - Negative numbers are not palindrome.
        - Numbers ending with 0 (except 0 itself) are not palindrome.
        - Reverse only half of the number and compare.
        """

        # Edge cases
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0

        # Reverse half of the number
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        # Check for even and odd digit numbers
        return x == reversed_half or x == reversed_half // 10
