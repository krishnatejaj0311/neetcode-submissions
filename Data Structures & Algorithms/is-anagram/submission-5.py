class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        setA = sorted(s.lower()) #alphabetical key1
        setB = sorted(t.lower()) #alphabetical key2

        s1 = ''.join(setA)
        s2 = ''.join(setB)

        # print(s1)
        # print(s2)
        return s1 == s2