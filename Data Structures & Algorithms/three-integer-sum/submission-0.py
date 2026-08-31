class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solution: List[List[int]] = []
        nums.sort()

        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # cant reach 0 sum if sorted and beyond 0 value:
            if num > 0:
                break

            start = i + 1
            end = len(nums) - 1

            while start < end:
                sum_ = num + nums[start] + nums[end]
                if sum_ == 0:
                    solution.append([num, nums[start], nums[end]])
                    
                    start += 1
                    end -= 1

                    while start < end and nums[start] == nums[start-1]:
                        start += 1

                    while start < end and nums[end] == nums[end+1]:
                        end -= 1
                else:
                    if sum_ < 0:
                        start += 1
                    else:
                        end -= 1
        
        return solution


