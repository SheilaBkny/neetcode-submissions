class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        # create map for t
        countT = {}
        for c in t:
            if c in countT:
                countT[c] += 1
            else:
                countT[c] = 1

        need = len(countT)
        # create map for the windows in s
        countS = {}
        left = 0
        have = 0
        res = ""


        for right in range(len(s)):
            # add right to window
            if s[right] in countS:
                countS[s[right]] += 1
            else:
                countS[s[right]] = 1
            
            # update have variable
            if s[right] in countT and countS[s[right]] == countT[s[right]]:
                have += 1

            # testing is valid window
            while have == need:
                # update res
                n = s[left: right + 1]
                if res == "" or len(res) >= len(n):
                    res = n
                # update have variable
                if s[left] in countT and countS[s[left]] == countT[s[left]]:
                    have -= 1
                countS[s[left]] -=1
                # shrink left
                left += 1

        return res








