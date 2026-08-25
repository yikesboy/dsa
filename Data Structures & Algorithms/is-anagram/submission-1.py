class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        occurences = {}

        for ch in s:
            occurences[ch] = occurences.get(ch,0) + 1
        
        for ch in t:
            if occurences.get(ch) == None or occurences.get(ch) == 0:
                return False
            
            newval = occurences.get(ch) - 1
            if newval == 0:
                del occurences[ch]
            else:
                occurences[ch] = newval

        if len(occurences) > 0:
            return False
        
        return True