class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0 
        start = 0
        end = len(height) - 1
        leftMax = 0
        rightMax = 0

        while start < end:
            sp_height = height[start]
            ep_height = height[end]

            if height[start] < height[end]:
                if leftMax < sp_height:
                    leftMax = sp_height
                else:
                    water += leftMax - sp_height
                start += 1
            else:
                if rightMax < ep_height:
                    rightMax = ep_height
                else:
                    water += rightMax - ep_height
                end -= 1
        
        return water
            

                
