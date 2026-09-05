class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        hashmaps = {}
        hashmapt = {}
        if len(s) != len(t):
            return False
        else:
            for i in range(len(s)):
                hashmaps[s[i]] = hashmaps.get(s[i],0) + 1
                hashmapt[t[i]] = hashmapt.get(t[i],0) + 1
        return hashmaps == hashmapt
                

        