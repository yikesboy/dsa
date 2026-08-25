class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keys = {}
        
        sorted_strings = [None] * len(strs)
        for i, string in enumerate(strs):
            sorted_strings[i] = "".join(sorted(string))
        
        for i, ss in enumerate(sorted_strings):
            if ss not in keys:
                keys[ss] = []
            
            keys[ss].append(strs[i])
        
        return list(keys.values())

        