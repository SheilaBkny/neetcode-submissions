class Solution:

    def encode(self, strs: List[str]) -> str:
        # add a # in the middle of each 
        s = ""
        for c in strs:
            s = s + str(len(c)) + "#" + c
        print(s)
        return s

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            word = s[j + 1: length + j + 1]
            res.append(word)
            i = length + j + 1
        return res
        

