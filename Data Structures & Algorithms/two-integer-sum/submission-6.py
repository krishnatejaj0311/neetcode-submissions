class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return 
        
        result = []
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    result.append([i, j])
        

        return sorted(result.pop())
