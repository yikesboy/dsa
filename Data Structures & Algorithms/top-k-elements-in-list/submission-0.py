class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occs = {}

        for num in nums:
            occs[num] = occs.get(num, 0) + 1

        top_k = sorted(occs.items(), key=lambda x: x[1], reverse=True)[:k]

        return [num for num, count in top_k]