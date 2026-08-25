class Solution:

    def encode(self, strs: List[str]) -> str:
        msg = ""
        for s in strs:
            msg += (str(len(s)) + "#") + s
        
        return msg


    def decode(self, s: str) -> List[str]:
        result: List[str] = []
        i = 0

        while i < len(s):
            j = i

            while j < len(s):
                if s[j] == "#":
                    break
                j += 1
            
            length = int(s[i:j])
            result.append(s[j+1:j+1+length])

            i = j+1+length

        return result
        
        

