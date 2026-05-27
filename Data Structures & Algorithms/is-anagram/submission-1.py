class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        '''
        plan:
        the letters in s1 are the same letters in s2
        add one word o hashmap
        then remove each letter according to other word.
        return true if dictionary is empty
        '''

        d = {}
        for l in s:
            if l in d:
                d[l] += 1
            else:
                d[l] = 1

        for l in t:
            if l in d:
                if d[l] - 1 == 0:
                    del d[l]
                else:
                    d[l] -= 1
            else:
                return False
            
        return not d
        