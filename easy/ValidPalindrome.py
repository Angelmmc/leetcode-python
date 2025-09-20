import re


class Solution:
    @staticmethod
    def is_palindrome(s: str) -> bool:
        clean_str = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        left_word = ""
        right_word = ""

        left = 0
        right = len(clean_str) - 1

        while left < len(clean_str):
            left_word = left_word + clean_str[left]
            right_word = right_word + clean_str[right]

            left += 1
            right -= 1

        if left_word != right_word:
            return False

        return True


print(Solution.is_palindrome("A man, a plan, a canal: Panama"))
print(Solution.is_palindrome("race a car"))
print(Solution.is_palindrome(" "))
