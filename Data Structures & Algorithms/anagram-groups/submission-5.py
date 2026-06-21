class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []

        if not strs:
            return []
        
        else:

            anagram_hash_map = {}
            for each_word in strs:
                anagram_key = ''.join(sorted(each_word.lower()))
                if anagram_key not in anagram_hash_map:
                    anagram_hash_map[anagram_key] = [each_word]
                else:
                    anagram_hash_map[anagram_key].append(each_word)
            
            for anagram_keys in anagram_hash_map:
                output.append(anagram_hash_map[anagram_keys])
            
            return output
    