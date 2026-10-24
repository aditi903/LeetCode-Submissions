class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        TotalArea = 0
        while left < right:
            if height[left] < height[right]:
                length = height[left]
                breadth = right - left 
                area = length * breadth
                TotalArea = max(TotalArea, area)
                left += 1
            elif height[left] > height[right]:
                length = height[right]
                breadth = right - left 
                area = length * breadth
                TotalArea = max(TotalArea, area)
                right -= 1
            else:
                length = height[left]
                breadth = right - left 
                area = length * breadth
                TotalArea = max(TotalArea, area)
                left += 1
                right -= 1
        return TotalArea