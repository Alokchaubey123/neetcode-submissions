class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # return Counter(s) == Counter(t)
        return "".join(sorted(s)) == "".join(sorted(t))
        if len(s) != len(t):
            return False
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[j[i]] = 1+countS.get(j[i], 0)
            countT[k[i]] = 1+countT.get(k[i], 0)
        # for c in countS:
        #     if countS[c] != countT.get(c,0):
        #         return False
        return countS == countT