class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        
        current_length = 1
        max_length = 1

        nums_sorted = sorted(list(set(nums))) #remove duplicates
        for i in range(1, len(nums_sorted)):
            if nums_sorted[i] - nums_sorted[i-1] == 1:
                current_length += 1
            else:
                max_length = max(current_length, max_length)
                current_length = 1
        return max(max_length, current_length)

