class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_counts = {}
        t_counts = {}
        for i in s:
            s_counts[i] = s_counts.get(i, 0) + 1

        for i in t:
            t_counts[i] = t_counts.get(i, 0) + 1
        
        if s_counts == t_counts :
            return True
        return False
