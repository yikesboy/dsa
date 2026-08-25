class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_seq = 0
        numbers = set(nums)

        for u in numbers:
            if (u-1) in numbers:
                continue

            current = u
            candidate_length = 1
            while (current + 1) in numbers:
                current += 1
                candidate_length += 1
                
            if candidate_length > longest_seq:
                longest_seq = candidate_length

        return longest_seq                 
