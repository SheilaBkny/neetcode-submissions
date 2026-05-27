class Solution:
    def isPalindrome(self, s: str) -> bool:
        b = ""
        for c in s:
            if c.isalpha() or c.isdigit():
                b += c

        b = b.lower()
        print(b)

        i, j = 0, len(b) - 1

        while i < j:
            if b[i] != b[j]:
                return False
            i+= 1
            j -= 1

        return True