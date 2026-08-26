class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashmap = {}
        for i,n in enumerate(nums):
            if n in hashmap:
                hashmap[n] = 1 + hashmap[n]
            else:
                hashmap[n] = 1
        keys = sorted(hashmap.keys(), key=lambda item: hashmap[item], reverse=True)
        L = []
        for i in range(k):
            value = keys[i]
            L.append(value)
        return L

       



        