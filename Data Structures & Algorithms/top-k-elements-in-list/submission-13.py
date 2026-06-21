class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return 
        
        if len(nums) == k:
            return nums
        

        else:
            output = []
            store_number_counts = {}
            for numbers in nums:
                if numbers not in store_number_counts:
                    store_number_counts[numbers] = 1
                else:
                    store_number_counts[numbers] += 1
            
            # Sort items by frequency in descending order
            sorted_items = sorted(store_number_counts.items(), key=lambda x: x[1], reverse=True)

            # Take the keys of the first k items
            for i in range(k):
                output.append(sorted_items[i][0])
            
            return output