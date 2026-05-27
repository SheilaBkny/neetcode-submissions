class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []

        groups = {}

        for word in strs:
            alph = [0] * 26
            for c in word:
                alph[ord(c) - 97] += 1

            if tuple(alph) in groups:
                groups[tuple(alph)].append(word)
            else:
                groups[tuple(alph)] = [word]

        for k, v in groups.items():
            res.append(v)
        return res




        