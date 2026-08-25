class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []

        if not strs:
            return None
        else:
            anagram_store = {}
            for each_word in strs:

                hash_key = ''.join(sorted(each_word.lower()))
                if hash_key not in anagram_store:
                    anagram_store[hash_key] = [each_word]
                else:
                    anagram_store[hash_key].append(each_word)
            
            for anagram_keys in anagram_store:
                output.append(anagram_store[anagram_keys])
        
        return output 