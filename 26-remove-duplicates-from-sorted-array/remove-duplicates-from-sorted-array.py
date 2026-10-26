class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0 
        j = i + 1
        k = 1

        while i < j and j < len(nums):
            if nums[i] == nums[j]:
                j = j + 1
            else:
                nums[i+1] = nums[j]
                i = i + 1
                j = j + 1
                k = k + 1
        return k 





        
