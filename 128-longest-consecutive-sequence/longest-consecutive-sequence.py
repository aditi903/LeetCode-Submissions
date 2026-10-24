class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numsset = set(nums)
        best = 0
        for num in numsset:
            if num - 1 not in numsset:
                curr = num
                streak = 1
                while curr + 1 in numsset:
                    curr = curr + 1
                    streak = streak + 1
                best = max(best, streak)
        return best 
        
        

            