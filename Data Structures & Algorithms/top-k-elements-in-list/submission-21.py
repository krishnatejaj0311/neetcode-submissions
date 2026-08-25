class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        output = []
        if not nums:
            return []
        if len(set(nums)) == k:
            return list(set(nums))
        else:

            counts = {}
            nums_sorted = sorted(nums)
            for each_number in nums_sorted:
                if each_number not in counts:
                    counts[each_number] = 1
                else:
                    counts[each_number] += 1
            
            # Group keys by their frequencies to handle duplicate counts
            freq_map = {}
            for num, freq in counts.items():
                if freq not in freq_map:
                    freq_map[freq] = []
                freq_map[freq].append(num)
            print(freq_map)
            counts_values = list(counts.values())
            counts_values_sorted = sorted(counts_values, reverse=True)
            
            i = 0
            seen_nums = set()
            while len(output) < k:
                current_freq = counts_values_sorted[i]
                for val in freq_map[current_freq]:
                    if val not in seen_nums:
                        output.append(val)
                        seen_nums.add(val)
                        if len(output) == k:
                            break
                i += 1
            
            return output