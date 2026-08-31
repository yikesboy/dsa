class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights) - 1

        maximum = 0

        while start < end:
            can_hold = (end - start) * min([heights[start], heights[end]])

            if can_hold > maximum:
                maximum = can_hold

            if heights[start] < heights[end]:
                start += 1
            else:
                end -= 1
            
        return maximum
        
    