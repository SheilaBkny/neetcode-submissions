class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        understand:
        given a list of strings groups them into a list of anagrams
        return a list of these groups.
        plan:
        have an array of length 26 for th 26 letters
        - for each word, count the characters that are present,
        - have a hashmap with key - group of anagrams
        '''
        res = defaultdict(list) # mapping char count to list of anagrams

        for s in strs:
            count = [0] * 26 # initializing an array of length 26.
            for c in s:
                count[ord(c) - ord("a")] += 1 # ascii values
            res[tuple(count)].append(s) # lists cannot be keys, so make it
                        #into a tuple

        return res.values()
        


