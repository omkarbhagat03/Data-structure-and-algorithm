"""7. Reverse Integer
🧩 Problem Statement :-Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range
[-2³¹, 2³¹ − 1], then return 0.

📌 Examples

Example :-Input:  x = 123
Output: 321
Example :-Input:  x = -123
Output: -321

code:- """
class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)

        rev = 0
        while x != 0:
            digit = x % 10
            rev = rev * 10 + digit
            x //= 10

        rev *= sign

        if rev < -2**31 or rev > 2**31 - 1:
            return 0

        return rev

#time complexity :-O(log10(n))
#space complexity :-O(1)
