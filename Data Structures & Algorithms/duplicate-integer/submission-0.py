class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        occs = set(nums)
        if len(occs) != len(nums):
            return True
        return False
        