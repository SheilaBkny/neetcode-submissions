class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        # print(s[l])

        while l <= r:
            if s[l].isalnum() and s[r].isalnum():
                if s[l].lower() != s[r].lower():
                    print(s[l], s[r])
                    return False
            
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -=1
                continue
            print(s[l], s[r])
            l += 1
            r -=1

        return True


