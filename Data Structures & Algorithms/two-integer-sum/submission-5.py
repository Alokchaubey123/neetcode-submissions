class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        prevmap = {} # key value pairs

        for i , n in enumerate(nums):
            diff = target - n
            if diff in prevmap:
                return [prevmap[diff], i]
            prevmap[n] = i
        return

        # L = []
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if (nums[i] + nums[j]) == target:
        #             L.append(i)
        #             L.append(j)
        # return L
        
                    
        