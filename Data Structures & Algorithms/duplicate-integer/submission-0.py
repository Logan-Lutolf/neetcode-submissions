class Solution:
    
    
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Dictionary for values
        dict = {}

        for i in range(len(nums)):
            # Check dictionary for element
            if (nums[i] in dict): return True
            dict[nums[i]] = 1

        return False

