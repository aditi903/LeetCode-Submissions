class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]: 
                continue
            head = i
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sumtotal = nums[head] + nums[left] + nums[right]
                if sumtotal < 0:
                    left += 1
                elif sumtotal > 0:
                    right -= 1
                else:
                    result.append([nums[head], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return result
                    
                    
                
                
                

            
